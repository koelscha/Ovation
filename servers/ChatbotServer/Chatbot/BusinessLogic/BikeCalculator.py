from BusinessLogic import BusinessLogic


class BikeCalculator(BusinessLogic):
    def processEntities(self, entities):
        price = int(self.getValueByName(entities, 'price'))
        if price > 1000:
            return "We can include your bicycle into the household insurance for 11€ per year. Do you agree?"
        else:
            return "Bikes are included up to a value of {} €".format(price)
