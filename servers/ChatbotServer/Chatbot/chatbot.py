import json

from BusinessCase import BusinessCase, State
#from IntentClassifiers.RasaClassifier import RasaClassifier
from IntentClassifiers.SimpleClassifier import SimpleClassifier


class ChatBot:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.config = json.load(f)
        businessCases = [BusinessCase(b) for b in self.config["businessCases"]]
        self.businessCases = {b.intent: b for b in businessCases}
        self.currentBusinessCase = None
        self.intentClassifier = SimpleClassifier()

    def processMessage(self, message, clientId, attachments=None):
        result = None

        if not self.currentBusinessCase:
            intent = self.intentClassifier.classify(message)
            self.currentBusinessCase = self.businessCases[intent]

        if self.currentBusinessCase.state is State.confirmed:
            self.currentBusinessCase = None
            result = self.processMessage(message,clientId, attachments)
        else:
            result = self.currentBusinessCase.processMessage(message, clientId, attachments)

        return result
