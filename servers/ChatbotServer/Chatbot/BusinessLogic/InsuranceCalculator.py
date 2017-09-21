from BusinessLogic.BusinessLogic import BusinessLogic

class InsuranceCalculator(BusinessLogic):
    def processEntities(self, entities):
        return ("We updated your address to {}, {} {}\n"
        "Based on {} square meters the annual fee for your household insurance will be 56€ (previously 52€) "
        "starting from {}.").format(self.getValueByName(entities, 'street'),
                                  self.getValueByName(entities, 'zip'),
                                  self.getValueByName(entities, 'city'),
                                  self.getValueByName(entities, 'area'),
                                  self.getValueByName(entities, 'date'))

    def getValueByName(self, entities, name):
        for entity in entities:
            if entity.name == name:
                return entity.value
        return "unknown entity: {}".format(name)

