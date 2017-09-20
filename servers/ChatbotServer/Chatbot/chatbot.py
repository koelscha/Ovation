from flask import Flask, request
from flask_restful import Resource, Api
import requests
import urllib.parse as urlparse
import json
from enum import Enum

import IntentClassifier
from BusinessCase import BusinessCase
from Entity import Entity

app = Flask(__name__)
api = Api(app)



serverAddress = "192.168.54.37:8080"
#serverAddress = "127.0.0.1:8080"
chatBotAddress = "192.168.54.32:5000"

http = requests.Session()
headers = {'content-type': 'application/json'}
myEndpoint = {'url': urlparse.urlunparse(('http', chatBotAddress, '/message', '', '', ''))}
serverRegister = urlparse.urlunparse(('http', serverAddress, '/chatbot', '', '', ''))
serverMessage = urlparse.urlunparse(('http', serverAddress, '/message', '', '', ''))


def register():
    r = http.post(serverRegister, data=json.dumps(myEndpoint), headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Request failed with http status ' + str(r.status_code))


class State(Enum):
    init = 1
    extract = 2


class ChatBot(Resource):
    __name__ = "ChatBot"
    def __init__(self):
        self.state = State.init
        entities = [Entity("What is your name?", lambda message: message)]
        self.businessCases = {"greeting": BusinessCase(confirmationPhrase="How can help you?"),
                              "contract": BusinessCase(entities, confirmationPhrase="Your name is {}.")}
        self.currentBusinessCase = None
        self.currentEntity = None


    def onMessageReceived(self, message, clientId):
        if self.state is State.init:
            intent = IntentClassifier.classify(message)
            self.currentBusinessCase = self.businessCases[intent]
            self.state = State.extract
            self.currentEntity = self.currentBusinessCase.getNextEmptyEntity()

            if self.currentEntity:
                self.sendMessage(clientId, self.currentEntity.question)
                self.state = State.extract
        elif self.state is State.extract:
            self.currentEntity.value = self.currentEntity.extract(message)
            self.currentEntity = self.currentBusinessCase.getNextEmptyEntity()

        if not self.currentEntity:
            self.sendMessage(clientId, self.currentBusinessCase.confirmationPhrase)
            self.currentBusinessCase = None


    def sendMessage(selfs, clientId, message):
        data = {'clientId': clientId, 'message': message}
        print("Message sent: " + json.dumps(data))
        #r = http.post(serverMessage, data=json.dumps(data), headers=headers)
        #try:
        #    r.raise_for_status()
        #except requests.exceptions.HTTPError:
        #    print('Request failed with http status ' + str(r.status_code))

    def post(self):
        message, clientId = request.get_json()["message"], request.get_json()["clientId"]
        self.onMessageReceived(message, clientId)

chatbot = ChatBot()

api.add_resource(chatbot, '/message')


if __name__ == '__main__':
    try:
        #register()
        app.run(host='0.0.0.0')
    except:
        pass
