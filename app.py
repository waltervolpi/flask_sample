from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

import datetime


class HelloWorld(Resource):
    def get(self):
        data_s=str(datetime.datetime.now())
        return {'hello': data_s}

app = Flask(__name__)
CORS(app)
api = Api(app)


api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host="0.0.0.0")
