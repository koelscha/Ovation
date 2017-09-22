from EntityExtractors import EntityExtractor
from EntityExtractors import Match


class MirrorExtractor(EntityExtractor):
    def extractFromText(self, message, entities, currentEntity):
        if currentEntity:
            return [Match(currentEntity.name, message)]
        return []
