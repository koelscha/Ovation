import json

import IntentClassifier
from BusinessCase import BusinessCase, State


class ChatBot:
    def __init__(self, file_name):
        with open(file_name) as f:
            self.config = json.load(f)
        businessCases = [BusinessCase(b) for b in self.config["businessCases"]]
        self.businessCases = {b.intent: b for b in businessCases}
        self.currentBusinessCase = None

    def processMessage(self, message, clientId, attachments=None):
        result = None

        if not self.currentBusinessCase:
            intent = IntentClassifier.classify(message)
            self.currentBusinessCase = self.businessCases[intent]

        if self.currentBusinessCase.state is State.confirmed:
            self.currentBusinessCase = None
        else:
            result = self.currentBusinessCase.processMessage(message, clientId, attachments)

        return result
