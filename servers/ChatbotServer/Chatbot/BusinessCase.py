import importlib
from enum import Enum

from Entity import Entity


class State(Enum):
    init = 1
    waitForAnswer = 2
    waitForConfirm = 3
    confirmed = 4

class BusinessCase:
    counter = 0

    def __init__(self, config):
        self.name = config["name"]
        self.intent = config["intent"]
        self.entities = [Entity(e) for e in config["entities"]]
        module = importlib.import_module("BusinessLogic." + config["businessLogic"])
        self.businessLogic = getattr(module, config["businessLogic"])()
        self.confirmationPhrase = config["confirmationPhrase"]
        self.openingQuestion = config["openingQuestion"]
        self.state = State.init
        self.currentEntity = None

    def processMessage(self, message, clientId, attachments):
        if self.state is State.init:
            self.state = State.waitForAnswer
            return self.openingQuestion
        elif self.state is State.waitForAnswer:
            self.extractEntities(message, attachments)
            self.currentEntity = self.getNextEmptyEntity()

            if not self.currentEntity:
                self.state = State.waitForConfirm
                return self.businessLogic.processEntities(self.entities)
            else:
                self.state = State.waitForAnswer
                return self.currentEntity.question

        elif self.state is State.waitForConfirm:
            self.state = State.confirmed
            return self.confirmationPhrase

    def extractEntities(self, message, attachments):
        if self.currentEntity:
            self.currentEntity.value = self.currentEntity.extractor.extractFromText(message)
        else:
            pass  # later general entity extractor

    def getNextEmptyEntity(self):
        if not self.entities:
            return None
        for entity in self.entities:
            if not entity.value:
                return entity
        return None