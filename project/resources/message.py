from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from telegrambot.bot import TelegramBot

todos = {}


class Message(Resource):
    parser = reqparse.RequestParser()
    telegram = TelegramBot()

    def get(self):
        pass

    def post(self):
        to = request.form["to"]
        message = request.form["message"]

        self.telegram.bot.send_message(chat_id=to, text=message)




