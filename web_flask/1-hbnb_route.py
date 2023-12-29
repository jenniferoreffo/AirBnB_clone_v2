#!/usr/bin/python3

#-*-coding: utf-8-*-

""" A script to start a flask application """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Starts basic Flash web application"""
    return 'Hello HBNB!'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Add specific route /hbnb"""
    return 'HBNB!'
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

