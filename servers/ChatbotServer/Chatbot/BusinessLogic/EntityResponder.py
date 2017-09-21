from BusinessLogic.BusinessLogic import BusinessLogic


class EntityResponder(BusinessLogic):
    def processEntities(self, entities):
        return ",".join([entity.value for entity in entities])
