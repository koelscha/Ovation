from EntityExtractors import EntityExtractor
from EntityExtractors import Match


class MirrorExtractor(EntityExtractor):
    def extractFromText(self, message, entities):
        return [Match(entities[0], message)]
