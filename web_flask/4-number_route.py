#!/usr/bin/python3

#-*-coding: utf-8-*-

""" A script to start a flask application """

from flask import Flask, render_template_string

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
def show_c(text):
    text = text.replace('_', ' ')
    return f'C {text}'

@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python(text):
    text = text.replace('_', ' ')
    return f'Python {text}'
@app.route('/number/<int:n>')
def show_number(n):
    return f'{n} is a number'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

