from flask import Flask, request
from flask_restful import Resource, Api
import requests
import urllib.parse as urlparse
import json


app = Flask(__name__)
api = Api(app)



serverAddress = "192.168.54.37:8080"
#serverAddress = "127.0.0.1:8080"

http = requests.Session()
headers = {'content-type': 'application/json'}
myEndpoint = {'url': 'http://192.168.54.26:5000/message'}
serverRegister = urlparse.urlunparse(('http', serverAddress, '/chatbot', '', '', ''))
serverMessage = urlparse.urlunparse(('http', serverAddress, '/message', '', '', ''))


def register():
    r = http.post(serverRegister, data=json.dumps(myEndpoint), headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print('Request failed with http status ' + str(r.status_code))



class ChatBot(Resource):
    def onMessageReceived(self, message, clientId):
        print(message)
        print(clientId)
        data = {'clientId': '1', 'message': 'test'}

        r = http.post(serverMessage, data=json.dumps(data), headers=headers)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Request failed with http status ' + str(r.status_code))


    def post(self):
        message, clientId = request.get_json()["message"], request.get_json()["clientId"]
        self.onMessageReceived(message, clientId)


api.add_resource(ChatBot, '/message')


if __name__ == '__main__':
    try:
        register()
        app.run(host='0.0.0.0')
    except:
        pass
