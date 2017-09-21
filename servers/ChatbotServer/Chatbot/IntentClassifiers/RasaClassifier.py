from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Interpreter

from IntentClassifiers import IntentClassifier


class RasaClassifier(IntentClassifier):
    def __init__(self, rasa_model_dir, rasa_config_file):
        self.interpreter = Interpreter.load(rasa_model_dir, RasaNLUConfig(rasa_config_file))

    def classify(self, message):
        return self.interpreter.parse(message, "utf-8")['intent']['name']
