from enum import Enum

import IntentClassifier
from BusinessCase import BusinessCase
from Entity import Entity


class State(Enum):
    init = 1
    waitingForAnswer = 2


class ChatBot:
    def __init__(self):
        self.state = State.init
        entities = [Entity("What is your name?", lambda message: message)]
        self.businessCases = {"greeting": BusinessCase(confirmationPhrase="How can help you?"),
                              "contract": BusinessCase(entities, confirmationPhrase="Your name is {}.")}
        self.currentBusinessCase = None
        self.currentEntity = None


    def processMessage(self, message, clientId):
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
                self.currentEntity.value = self.currentEntity.extract(message)
                self.currentEntity = self.currentBusinessCase.getNextEmptyEntity()
                if self.currentEntity:
                    result = self.currentEntity.question

        if not result: # and not self.currentEntity:
            assert(not self.currentEntity)
            result = self.currentBusinessCase.confirmationPhrase
            self.currentBusinessCase = None

        return result