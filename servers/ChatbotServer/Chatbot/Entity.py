import importlib

class Entity:
    def __init__(self, config):
        self.name = config["name"]
        self.question = config["question"]
        if "extractor" in config:
            module = importlib.import_module("EntityExtractors." + config["extractor"])
            self.extractor = getattr(module, config["extractor"])()
        else:
            self.extractor = None
        self.value = None
        self.confidence = None