from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from ..telegrambot.bot import TelegramBot


class Message(Resource):
    parser = reqparse.RequestParser()
    telegram = TelegramBot()

    def get(self):
        return list(map(lambda a: a.to_dict(), self.telegram.get_messages()))

    def post(self):
        to = request.form["to"]
        message = request.form["message"]

        self.telegram.send_message(to, message)




