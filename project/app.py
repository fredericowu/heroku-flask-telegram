from flask import Flask, request
from flask_restful import Resource, Api
from resources.message import Message
from telegrambot.bot import TelegramBot

app = Flask(__name__)
api = Api(app)

api.add_resource(Message, '/api/message')

if __name__ == '__main__':
    app.run(debug=True)
