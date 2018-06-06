# heroku-flask-telegram
Telegram bot as a service on Heroku


## Setup you Bot

### First steps
- Create an account on Heroku.com.
- Create a Telegram Bot using the Bot Father. Just open the Telegram app on your phone and look for @BotFather and follow the steps. The important thing about this step is to keep the TOKEN that it gives you after you create your bot.


### Clone this repo
```sh
git clone https://github.com/fredericowu/heroku-flask-telegram
cd heroku-flask-telegram
```

### Setup Heroku
```
heroku login
heroku create
heroku heroku config:set TELEGRAM_TOKEN="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
git push heroku master

heroku open

heroku scale web=1

# to see the log screen
heroku logs --tail

```
 
