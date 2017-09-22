from BusinessLogic import BusinessLogic

class InsuranceCalculator(BusinessLogic):
    def processEntities(self, entities):
        return ("We updated your address to {} {}, {} {}\n"
        "Based on {} square meters the annual fee for your household insurance will be 56€ (previously 52€) "
        "starting from {}. \n\nIs there anything else I can do for you?").format(self.getValueByName(entities, 'street'),
                                    self.getValueByName(entities, 'streetnumber'),
                                    self.getValueByName(entities, 'zip'),
                                    self.getValueByName(entities, 'city'),
                                    self.getValueByName(entities, 'area'),
                                    self.getValueByName(entities, 'date'))


