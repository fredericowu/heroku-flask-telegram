from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from ..telegrambot.bot import TelegramBot
import os


class Message(Resource):
    parser = reqparse.RequestParser()
    telegram = TelegramBot()

    def get(self):
        return list(map(lambda a: [a[0], a[1] if a[0] == "out" else a[1].to_dict(), a[2]], self.telegram.get_messages()))

    def post(self):
        to = request.form["to"]
        message = request.form["message"]

        self.telegram.send_message(to, message)




