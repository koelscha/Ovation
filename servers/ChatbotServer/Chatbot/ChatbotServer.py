from flask import Flask, request
from flask_restful import Resource, Api
import requests
import urllib.parse as urlparse
import json

from chatbot import ChatBot


class ChatbotServer:
    chatbot = ChatBot()

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(MessageHandler, '/message')

        self.serverAddress = "192.168.54.37:8080"
        #self.serverAddress = "127.0.0.1:8080"
        self.chatBotAddress = "192.168.54.32:5000"

        self.myMessageURL = {'url': urlparse.urlunparse(('http', self.chatBotAddress, '/message', '', '', ''))}
        self.smoopeRegisterURL = urlparse.urlunparse(('http', self.serverAddress, '/chatbot', '', '', ''))
        self.smoopeMessageURL = urlparse.urlunparse(('http', self.serverAddress, '/message', '', '', ''))


    def register(self):
        http = requests.Session()
        headers = {'content-type': 'application/json'}
        response = http.post(self.smoopeRegisterURL, data=json.dumps(self.myMessageURL), headers=headers)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Request failed with http status ' + str(response.status_code))


    def start(self):
        #self.register()
        self.app.run(host='0.0.0.0')


class MessageHandler(Resource):
    def post(self):
        message, clientId = request.get_json()["message"], request.get_json()["clientId"]
        self.onMessageReceived(message, clientId)

    def onMessageReceived(self, message, clientId):
        answer = ChatbotServer.chatbot.processMessage(message, clientId)
        self.sendMessage(clientId, answer)

    def sendMessage(selfs, clientId, message):
        data = {'clientId': clientId, 'message': message}
        print("Message sent: " + json.dumps(data))
        # r = http.post(serverMessage, data=json.dumps(data), headers=headers)
        # try:
        #    r.raise_for_status()
        # except requests.exceptions.HTTPError:
        #    print('Request failed with http status ' + str(r.status_code))


if __name__ == '__main__':
    ChatbotServer().start()
