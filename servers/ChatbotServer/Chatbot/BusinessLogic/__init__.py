class BusinessLogic:
    def processEntities(self, entities):
        pass

    def getValueByName(self, entities, name):
        for entity in entities:
            if entity.name == name:
                return entity.value
        return "unknown entity: {}".format(name)
