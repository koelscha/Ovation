import spacy

from EntityExtractors import EntityExtractor
from EntityExtractors import Match
import spacyEnd

class SpacyExtractor(EntityExtractor):
    nlp = spacy.load('en')

    def extractFromText(self, message, entityTypes, currentEntity):
        resultTuple =spacyEnd.main('../../../../models/model_synth_street','street-name', message)
        return []
