from Entity import Entity

class BusinessCase:
    def __init__(self, config):
        self.name = config["name"]
        self.entities = [Entity(e) for e in config["entities"]]
        self.businessLogic = config["businessLogic"]
        self.confirmationPhrase = config["confirmationPhrase"]

    def getNextEmptyEntity(self):
        if not self.entities:
            return None
        for entity in self.entities:
            if not entity.value:
                return entity
        return None