#!/usr/bin/env python3
""" This module creates a Flask app """
from flask import Flask, g, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    """ Returns the index.html page """
    return render_template("5-index.html")


@babel.localeselector
def get_locale():
    """ Gets the locale from query string or request.accept_languages """
    locale = request.args.get("locale")
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(user_id):
    """ Returns the user based on user_id """
    return users.get(user_id)


@app.before_request
def before_request():
    """ Checks for login_as passed in query string and sets attributes """
    user_id = request.args.get("login_as")
    if user_id is not None:
        user_id = int(user_id)
    g.user = get_user(user_id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
