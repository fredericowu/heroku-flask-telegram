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
    the_time = datetime.datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

