from BusinessLogic import BusinessLogic


class BikeCalculator(BusinessLogic):
    def processEntities(self, entities):
        price = float(self.getValueByName(entities, 'price').split("€")[0].replace(",", "."))
        if price > 1000:
            return("Ihr Fahrrad ist aktuell nicht versichert. Ich kann Ihnen jedoch eine Zusatz-Versicherung für 11€ pro Jahr anbieten. Soll ich Ihnen ein Angebot zuschicken?")
        else:
            return("Fahrräder sind bis zu einem Wert von 1000€ versichert. Sie müssen sich also keine Sorgen machen.")
