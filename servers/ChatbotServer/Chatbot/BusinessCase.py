import BusinessLogic
from Entity import Entity
from BusinessLogic import InsuranceCalculator

class BusinessCase:
    def __init__(self, config):
        self.name = config["name"]

        self.entities = [Entity(e) for e in config["entities"]]

        module = getattr(BusinessLogic, config["businessLogic"])
        self.businessLogic = getattr(module, config["businessLogic"])()
        self.confirmationPhrase = config["confirmationPhrase"]
        self.intent = config["intent"]

    def getNextEmptyEntity(self):
        if not self.entities:
            return None
        for entity in self.entities:
            if not entity.value:
                return entity
        return None