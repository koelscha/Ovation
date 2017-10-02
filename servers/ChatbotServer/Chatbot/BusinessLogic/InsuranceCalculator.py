from BusinessLogic import BusinessLogic

class InsuranceCalculator(BusinessLogic):
    def processEntities(self, entities):
        return ("Wir haben Ihre Adresse ab " + self.getValueByName(entities, 'date') + " geändert:\n" + self.getValueByName(entities, 'street') + " " + self.getValueByName(entities, 'streetnumber') + ", " + self.getValueByName(entities, 'zip') + " " + self.getValueByName(entities, 'city') + ".\nFür Ihre " + self.getValueByName(entities, 'area') + " Quadratmeter große Wohnung wird die jährliche Rate 56€ betragen (vorher 52€).\nKann ich sonst noch etwas für Sie tun?")
