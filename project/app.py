from flask import Flask, request
from flask_restful import Resource, Api
from .resources.message import Message
import os
import datetime


app = Flask(__name__)
api = Api(app)

api.add_resource(Message, '/api/message')


@app.route('/')
def homepage():
    return "Hi, better page coming soon"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

