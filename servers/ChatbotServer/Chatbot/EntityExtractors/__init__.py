class EntityExtractor:
    def extractFromText(self, message, entities):
        pass

    def extractFromImage(self, attachment, entities):
        extractedEntities = []
        extractedEntities.append(Match("name", "Marc"))
        extractedEntities.append(Match("street", "Burggrafenstr.", 1))
        extractedEntities.append(Match("streetnumber", "61", 1))
        extractedEntities.append(Match("zip", "10787", 1))
        extractedEntities.append(Match("city", "Berlin", 1))
        extractedEntities.append(Match("country", "Deutschland", 1))
        extractedEntities.append(Match("date", None, 1))
        extractedEntities.append(Match("area", 67, 1))
        return [match for match in extractedEntities if match.name in entities]


class Match():
    def __init__(self, name, value, confidence=None):
        self.name = name
        self.value = value
        self.confidence = confidence