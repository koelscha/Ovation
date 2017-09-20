class BusinessCase:
    def __init__(self, intent, entities=None, businessLogic=None, confirmationPhrase=""):
        self.intent = intent
        self.entities = entities
        self.businessLogic = businessLogic
        self.confirmationPhrase = confirmationPhrase

    def getNextEmptyEntity(self):
        if not self.entities:
            return None
        for entity in self.entities:
            if not entity.value:
                return entity
        return None