#!/usr/bin/env python3
"""
App FLASK
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def home():
    """
    home route
    """
    return render_template('0-index.html')