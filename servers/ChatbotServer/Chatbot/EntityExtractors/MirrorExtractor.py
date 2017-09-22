from EntityExtractors import EntityExtractor
from EntityExtractors import Match


class MirrorExtractor(EntityExtractor):
    def extractFromText(self, message, emptyEntities, currentEntity):
        if currentEntity:
            extractedEntities = {currentEntity.name: Match(currentEntity.name, message)}
            return self.postExtract(extractedEntities, emptyEntities)
        return []
