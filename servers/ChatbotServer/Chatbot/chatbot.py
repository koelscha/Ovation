import json

from BusinessCase import BusinessCase, State
from IntentClassifiers.RasaClassifier import RasaClassifier
from IntentClassifiers.SimpleClassifier import SimpleClassifier


class ChatBot:
    def __init__(self, file_name):
        self.clientSessions = {}
        self.config_file_name = file_name
        self.intentClassifier = RasaClassifier()

    def processMessage(self, message, clientId, attachments=None):
        result = None

        currentClientBusinessCase = self.getCurrentBusinessCase(clientId)
        if not currentClientBusinessCase:
            intent = self.intentClassifier.classify(message)
            self.setCurrentBusinessCase(clientId, intent)
            currentClientBusinessCase = self.getCurrentBusinessCase(clientId)

        if currentClientBusinessCase.state is State.confirmed:
            self.resetBusinessCase(clientId)
            result = self.processMessage(message, clientId, attachments)
        else:
            result = currentClientBusinessCase.processMessage(message, clientId, attachments)

        return result

    def getCurrentBusinessCase(self, clientId):
        return self.clientSessions[clientId] if clientId in self.clientSessions else None

    def setCurrentBusinessCase(self, clientId, intent):
        with open(self.config_file_name) as f:
            config = json.load(f)
        jsonBusinessCases = config["businessCases"]
        businessCasesForIntent = [jsonCase for jsonCase in jsonBusinessCases if jsonCase["intent"] == intent]
        newCase = BusinessCase(businessCasesForIntent[0]) if len(businessCasesForIntent) == 1 else None
        if not newCase:
            raise Exception("No business case registered for inten '"+ intent + "'")
        self.clientSessions[clientId] = newCase

    def resetBusinessCase(self, clientId):
        self.clientSessions.pop(clientId)
