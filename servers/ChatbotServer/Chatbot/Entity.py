class Entity:
    def __init__(self, config):
        self.name = config["name"]
        self.question = config["question"]
        self.value = None
        self.confidence = None