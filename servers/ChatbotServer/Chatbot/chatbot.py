from enum import Enum

import IntentClassifier
from BusinessCase import BusinessCase
from BusinessLogic import InsuranceCalculator
from Entity import Entity

from Downloader import download
import json


class State(Enum):
    init = 1
    waitingForAnswer = 2


class ChatBot:
    def __init__(self, filename):
        self.config = json.load(filename)
        self.state = State.init
        self.businessCases = [BusinessCase(b) for b in self.config["businessCases"]]
        self.currentBusinessCase = None
        self.currentEntity = None


    def processMessage(self, message, clientId, attachments):
        result = None

        if not self.currentBusinessCase:
            intent = IntentClassifier.classify(message)
            self.currentBusinessCase = self.businessCases[intent]
            self.currentEntity = self.currentBusinessCase.getNextEmptyEntity()

        if self.currentEntity:
            if self.state is State.init:
              result = self.currentEntity.question
              self.state =  State.waitingForAnswer
            else:
                self.currentEntity.value = self.currentEntity.extract(message, attachments)
                self.currentEntity = self.currentBusinessCase.getNextEmptyEntity()
                if self.currentEntity:
                    result = self.currentEntity.question

        if not result: # and not self.currentEntity:
            assert(not self.currentEntity)
            result = self.currentBusinessCase.confirmationPhrase
            self.currentBusinessCase = None

        return result

