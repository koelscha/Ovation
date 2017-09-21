import importlib

class Entity:
    def __init__(self, config):
        self.name = config["name"]
        self.question = config["question"]
        self.value = None
        self.confidence = None
        module = importlib.import_module("EntityExtractors." + config["extractor"])
        self.extractor = getattr(module, config["extractor"])()