import spacy

from EntityExtractors import EntityExtractor
from EntityExtractors import Match
import spacyEnd


class SpacyExtractor(EntityExtractor):
    nlp = spacy.load('en')

    def extractFromText(self, message, entityTypes, currentEntity):
        result = []
        _, area, _, streetname, _, streetnumber, _, zipcode = spacyEnd.main('../../../../models/model_synth_street',
                                                                            'street-name', message)

        if (area):
            result.append(Match("area", area, None))

        if (streetname):
            result.append(Match("street", streetname, None))

        if (streetnumber):
            result.append(Match("streetnumber", streetnumber, None))

        if (zipcode):
            result.append(Match("zip", zipcode, None))

        return result
