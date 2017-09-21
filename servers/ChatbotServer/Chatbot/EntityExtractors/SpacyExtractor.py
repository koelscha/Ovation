import spacy

import EntityExtractors.EntityExtractor


class SpacyExtractor(EntityExtractors.EntityExtractor):
    nlp = spacy.load('en')

    def extractFromText(self, message, entityTypes=None):
        extractedEntities = dict()
        for entity in self.nlp(message).ents:
            if not entityTypes or entity.label_ in entityTypes:
                if entity.label_ in extractedEntities:
                    extractedEntities[entity.label_] += [entity.text]
                else:
                    extractedEntities[entity.label_] = [entity.text]

        return extractedEntities
