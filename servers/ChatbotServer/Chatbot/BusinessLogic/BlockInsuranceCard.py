from BusinessLogic import BusinessLogic


class BlockInsuranceCard(BusinessLogic):
    def processEntities(self, entities):
        return ("Mr. Fisher. We blocked your insurance card for insurance number {}.\n"
                "We will send you immediately a new one, which you will find in your postbox "
                "within the next two working days.").format(self.getValueByName(entities, 'insuranceNo'))
