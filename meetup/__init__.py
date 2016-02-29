from flask import Flask
from meetup.users.views import users

app = Flask(__name__)
app.register_blueprint(users, url_prefix='/users')