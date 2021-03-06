import importlib
from Entity import Entity
from enum import Enum
from collections import OrderedDict

class State(Enum):
    init = 1
    waitForAnswer = 2
    waitForConfirm = 3
    confirmed = 4

class BusinessCase:
    def __init__(self, config):
        self.name = config["name"]
        self.intent = config["intent"]
        entities = [Entity(e) for e in config["entities"]] if "entities" in config else []
        self.entities = OrderedDict()
        for e in entities:
            self.entities[e.name] = e
        if "businessLogic" in config:
            module = importlib.import_module("BusinessLogic." + config["businessLogic"])
            self.businessLogic = getattr(module, config["businessLogic"])()
        else:
            self.businessLogic=None
        self.confirmationPhrase = config["confirmationPhrase"] if "confirmationPhrase" in config else None
        self.openingQuestion = config["openingQuestion"]
        self.state = State.init
        self.currentEntity = None
        if "extractor" in config:
            module = importlib.import_module("EntityExtractors." + config["extractor"])
            self.extractor = getattr(module, config["extractor"])()
        else:
            self.extractor = None

    def processMessage(self, message, clientId, attachments):
        if self.state is State.init:
            if self.extractor:
                self.state = State.waitForAnswer
            else:
                self.state = State.confirmed
            return self.openingQuestion
        elif self.state is State.waitForAnswer:
            self.extractEntities(message, attachments)
            self.currentEntity = self.getNextEmptyEntity()

            if not self.currentEntity:
                if not self.confirmationPhrase:
                    self.state=State.confirmed
                else:
                    self.state = State.waitForConfirm
                return self.businessLogic.processEntities(self.entities.values())
            else:
                self.state = State.waitForAnswer
                return self.currentEntity.question

        elif self.state is State.waitForConfirm:
            self.state = State.confirmed
            return self.confirmationPhrase


    def extractEntities(self, message, attachments):
        if attachments:
            for attachment in attachments:
                emptyEntities = self.getEmptyEntities()
                if self.currentEntity and self.currentEntity.extractor:
                    matchesForEntityExtractor = self.currentEntity.extractor.extractFromImage(attachment, emptyEntities, self.currentEntity)
                    for match in matchesForEntityExtractor:
                        self.entities[match.name].value = match.value
                        self.entities[match.name].confidence = match.confidence
                    emptyEntities = self.getEmptyEntities()

                matches = self.extractor.extractFromImage(attachment, emptyEntities, self.currentEntity)
                for match in matches:
                    self.entities[match.name].value = match.value
                    self.entities[match.name].confidence = match.confidence

        if message:
            emptyEntities = self.getEmptyEntities()
            if self.currentEntity and self.currentEntity.extractor:
                matchesForEntityExtractor = self.currentEntity.extractor.extractFromText(message, emptyEntities,
                                                                                          self.currentEntity)
                for match in matchesForEntityExtractor:
                    self.entities[match.name].value = match.value
                    self.entities[match.name].confidence = match.confidence
                emptyEntities = self.getEmptyEntities()
            
            matches = self.extractor.extractFromText(message, emptyEntities, self.currentEntity)

            for match in matches:
                self.entities[match.name].value = match.value
                self.entities[match.name].confidence = match.confidence


    def getNextEmptyEntity(self):
        if not self.entities:
            return None
        for entity in self.entities.values():
            if not entity.value:
                return entity
        return None

    def getEmptyEntities(self):
        if not self.entities:
            return None
        entities = []
        for entity in self.entities.values():
            if not entity.value:
                entities.append(entity.name)
        return entities