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
def display_c_text():
    modified_text = text.display('_', ' ')
    """Display c followed by the value of text, replace "_" with " "  """
    return f'C {modified_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

