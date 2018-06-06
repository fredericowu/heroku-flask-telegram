# heroku-flask-telegram
Telegram bot as a service on Heroku


## Setup your Bot

### First steps
- Create an account on Heroku.com.
- Create a Telegram Bot using the Bot Father. Just open the Telegram app on your phone, look for @BotFather and follow the steps. The important thing about this step is to keep in a safe place the TOKEN that it gives you after you create your bot.


### Clone this repo
```sh
$ git clone https://github.com/fredericowu/heroku-flask-telegram
$ cd heroku-flask-telegram
```

### Setup Heroku
```
$ heroku login
$ heroku create

$ git push heroku master

# XXXX... is the TOKEN given by the @BotFather
$ heroku heroku config:set TELEGRAM_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

$ heroku open

$ heroku scale web=1

# to see the log screen
$ heroku logs --tail

```

## Use your bot

### First say "Hi"
Look for your bot on the Telegram app and say something to it.

### Get the received messages

In the heroku-flask-telegram/ directory type:
```sh
$ APP_URL=$(heroku info -s | grep web_url | cut -d= -f2)

# This is the Heroku app URL
$ echo $APP_URL

$ curl ${APP_URL}"api/message"
[["out", "You said: Banana", "55736795"], ["in", {"message_id": 55, "date": 1528251472, "chat": {"id": 55736795, "type": "private", "username": "fredericowu", "first_name": "Frederico", "last_name": "Wu"}, "text": "Banana", "entities": [], "caption_entities": [], "photo": [], "new_chat_members": [], "new_chat_photo": [], "delete_chat_photo": false, "group_chat_created": false, "supergroup_chat_created": false, "channel_chat_created": false, "from": {"id": 55736795, "first_name": "Frederico", "is_bot": false, "last_name": "Wu", "username": "fredericowu", "language_code": "pt-br"}}, null]]
```
The received messages are going to be outputted in JSON format.

### Send messages
To send a message to someone the person must start the conversation first, otherwise it won't work.
You can reply the above these ways:

```sh
$ curl ${APP_URL}"api/message" -d "to=fredericowu&message=hey" -X POST
$ curl ${APP_URL}"api/message" -d "to=55736795&message=hi" -X POST
```

## Your own bot
Fork this repo and change as you wish.
To start it on your environment (not Heroku's) do as described below. 

In the heroku-flask-telegram/ directory type:

```sh
# Please, check if you have python 3
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pipenv install Pipenv
(venv) $ gunicorn -e "TELEGRAM_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" -w 1 -b 0.0.0.0:5000 project.app:app
```


