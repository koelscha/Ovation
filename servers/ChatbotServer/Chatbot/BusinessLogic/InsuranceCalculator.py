from BusinessLogic.BusinessLogic import BusinessLogic

class InsuranceCalculator(BusinessLogic):
    demoAnswer = "We can modify your household insurance according to the information you gave us beginning\
                  from 1st of October 2017. The new annual fee is 56€ for a 104 square meter flat in Berlin."

    def processEntities(self, entities):
        return InsuranceCalculator.demoAnswer


class EntityResponder(BusinessLogic):
    def processEntities(self, entities):
        return ",".join([entity.value for entity in entities])
