import argparse
import json
import threading
import urllib.parse as urlparse

import requests
from flask import Flask, request
from flask_restful import Resource, Api

from chatbot import ChatBot

parser = argparse.ArgumentParser()
parser.add_argument("json", type=str)
args = parser.parse_args()

class ChatbotServer:
    chatbot = ChatBot(args.json)
    serverAddress = "127.0.0.1:8080"
    #serverAddress = "192.168.54.37:8080"
    smoopeMessageURL = urlparse.urlunparse(('http', serverAddress, '/message', '', '', ''))

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(MessageHandler, '/message')

        self.chatBotAddress = "127.0.0.1:5000"
        #self.chatBotAddress = "192.168.54.26:5000"

        self.myMessageURL = {'url': urlparse.urlunparse(('http', self.chatBotAddress, '/message', '', '', ''))}
        self.smoopeRegisterURL = urlparse.urlunparse(('http', self.serverAddress, '/chatbot', '', '', ''))


    def register(self):
        http = requests.Session()
        headers = {'content-type': 'application/json'}
        response = http.post(self.smoopeRegisterURL, data=json.dumps(self.myMessageURL), headers=headers)
        try:
            response.raise_for_status()
            print('Sucessfully registered as chatbot to ' + self.smoopeRegisterURL)
        except requests.exceptions.HTTPError:
            print('Request failed with http status ' + str(response.status_code))


    def start(self):
        self.register()
        self.app.run(host='0.0.0.0')




class MessageHandler(Resource):
    def post(self):
        print("post")
        message, clientId, attachments = request.get_json()["message"], request.get_json()["clientId"], request.get_json()["attachments"]
        threading.Thread(target=self.onMessageReceived(message, clientId, attachments)).start()

    def onMessageReceived(self, message, clientId, attachments):
        answer = ChatbotServer.chatbot.processMessage(message, clientId, attachments)
        self.sendMessage(clientId, answer)

    def sendMessage(self, clientId, message):
        http = requests.Session()
        headers = {'content-type': 'application/json'}
        data = {'clientId': clientId, 'message': message}
        print("Message sent: " + json.dumps(data))

        response = http.post(ChatbotServer.smoopeMessageURL, data=json.dumps(data), headers=headers)
        try:
           response.raise_for_status()
        except requests.exceptions.HTTPError:
           print('Request failed with http status ' + str(response.status_code))


if __name__ == '__main__':
    ChatbotServer().start()
