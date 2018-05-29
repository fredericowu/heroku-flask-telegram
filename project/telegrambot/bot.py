from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import os
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

class TelegramBot():
    updater = None
    bot = None
    received = []
    pool_size = 100
    chats = {}

    def __init__(self, token=None):
        if TelegramBot.updater is None:
            if not token:
                token = os.environ.get("TELEGRAM_TOKEN")

            TelegramBot.updater = Updater(token=token)

            handlers = {
                CommandHandler: [
                    ('start', TelegramBot.start),
                ],
                MessageHandler: [
                    (Filters.text, TelegramBot.echo),
                    (Filters.text, TelegramBot.__received_message),
                ],
            }

            for handler_type in handlers:
                group = 0
                for handler in handlers[handler_type]:
                    handler_func = handler_type(*handler)
                    TelegramBot.updater.dispatcher.add_handler(handler_func, group)
                    group += 1

            TelegramBot.updater.start_polling()

        self.updater = TelegramBot.updater
        self.bot = self.updater.bot

    @classmethod
    def start(cls, bot, update):
        msg = "Hi, to know about me access https://github.com/fredericowu/heroku-flask-telegram"
        bot.send_message(chat_id=update.message.chat_id, text=msg)

    @classmethod
    def echo(cls, bot, update):
        msg = "You said: {0}".format(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text=msg)

    @classmethod
    def __received_message(cls, bot, update):
        user = update.message.from_user
        logger.info('You talk with user {} and his user ID: {} '.format(user['username'], user['id']))
        #print(user)
        cls.chats[user['id']] = user

        # TODO Let's not waste memory until we get a database
        if len(cls.received) > cls.pool_size:
            cls.received.pop(0)

        cls.received.append(update.message.text)


