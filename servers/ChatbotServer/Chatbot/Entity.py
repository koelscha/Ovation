class Entity:
    def __init__(self, question, entityExtractor):
        self.question = question
        self.value = None
        self.confidence = -1
        self.extract = entityExtractor