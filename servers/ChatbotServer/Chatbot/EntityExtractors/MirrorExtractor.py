from EntityExtractors.EntityExtractor import EntityExtractor


class MirrorExtractor(EntityExtractor):
    def extractFromText(self, message):
        return message
