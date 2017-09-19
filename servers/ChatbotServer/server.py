from flask import Flask, request
from flask_restful import Resource, Api

import time

app = Flask(__name__)
api = Api(app)


class Clock(Resource):
    def get(self):
        return {'time': time.strftime("%H:%M")}

api.add_resource(Clock, '/clock')

if __name__ == '__main__':
     app.run()
