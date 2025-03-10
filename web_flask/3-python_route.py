#!/usr/bin/python3

#-*-coding: utf-8-*-

""" A script to start a flask application """

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    """Starts basic Flash web application"""
    return 'Hello HBNB!'
@app.route('/hbnb')
def display_hbnb():
    """Add specific route /hbnb"""
    return 'HBNB!'
@app.route('/c/<text>', strict_slashes=False)
def c_text():
    return 'C ' + text.replace('_', ' ') 
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

