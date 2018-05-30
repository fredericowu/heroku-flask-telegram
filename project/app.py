from flask import Flask, request
from flask_restful import Resource, Api
from .resources.message import Message
from .telegrambot.bot import TelegramBot

app = Flask(__name__)
api = Api(app)

api.add_resource(Message, '/api/message')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print("Port", port)
    app.run(host='0.0.0.0', port=port, debug=True)

