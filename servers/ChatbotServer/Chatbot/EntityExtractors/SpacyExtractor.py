import spacy

from EntityExtractors.EntityExtractor import EntityExtractor
from EntityExtractors import Match

class SpacyExtractor(EntityExtractor):
    nlp = spacy.load('en')

    def extractFromText(self, message, entityTypes=None):
        extractedEntities = []
        for entity in self.nlp(message).ents:
            if not entityTypes or entity.label_ in entityTypes:
                if entity.label_ in extractedEntities:
                    extractedEntities[entity.label_] += [entity.text]
                else:
                    extractedEntities[entity.label_] = [entity.text]

        return extractedEntities


    def extractFromImage(self, attachment, entities):
        extractedEntities = []
        extractedEntities.append(Match("street", "Burggrafenstr.", 1))
        extractedEntities.append(Match("streetnumber", "61", 1))
        extractedEntities.append(Match("zipcode", "10787", 1))
        extractedEntities.append(Match("city", "Berlin", 1))
        extractedEntities.append(Match("country", "Deutschland", 1))
        extractedEntities.append(Match("date", None, 1))
        extractedEntities.append(Match("area", 67, 1))
        return [match for match in extractedEntities if match.name in entities]
