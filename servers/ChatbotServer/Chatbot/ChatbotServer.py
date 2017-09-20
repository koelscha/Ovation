from flask import Flask, request
from flask_restful import Resource, Api
import requests
import urllib.parse as urlparse
import json

from chatbot import ChatBot

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

chatbot = ChatBot()

def register():
    r = http.post(serverRegister, data=json.dumps(myEndpoint), headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Request failed with http status ' + str(r.status_code))

class ChatbotServer(Resource):
    def post(self):
        message, clientId = request.get_json()["message"], request.get_json()["clientId"]
        self.onMessageReceived(message, clientId)

    def onMessageReceived(self, message, clientId):
        answer = chatbot.processMessage(message, clientId)
        self.sendMessage(clientId, answer)

    def sendMessage(selfs, clientId, message):
        data = {'clientId': clientId, 'message': message}
        print("Message sent: " + json.dumps(data))
        # r = http.post(serverMessage, data=json.dumps(data), headers=headers)
        # try:
        #    r.raise_for_status()
        # except requests.exceptions.HTTPError:
        #    print('Request failed with http status ' + str(r.status_code))

api.add_resource(ChatbotServer, '/message')


if __name__ == '__main__':
    try:
        #register()
        app.run(host='0.0.0.0')
    except:
        pass
