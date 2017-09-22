import spacy

import spacyEnd
from EntityExtractors import EntityExtractor
from EntityExtractors import Match


class SpacyExtractor(EntityExtractor):
    nlp = spacy.load('en')

    def extractFromText(self, message, emptyEntities, currentEntity):
        result = dict()
        _, area, _, streetname, _, streetnumber, _, zipcode, _, date_ = spacyEnd.main(
            '../../../models/model_synth_street',
                                                                            'street-name', message)

        if (area):
            result["area"] = (Match("area", area, None))

        if (streetname):
            result["street"] = (Match("street", streetname, None))

        if (streetnumber):
            result["streetnumber"] = (Match("streetnumber", streetnumber, None))

        if (zipcode):
            result["zip"] = (Match("zip", zipcode, None))

        if date_:
            result["date"] = (Match("date", date_, None))

        return self.postExtract(result, emptyEntities)
