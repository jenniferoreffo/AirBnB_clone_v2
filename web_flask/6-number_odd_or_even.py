#!/usr/bin/python3

#-*-coding: utf-8-*-

""" A script to start a flask application """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """Starts basic Flash web application"""
    return 'Hello HBNB!'
@app.route('/hbnb')
def hbnb():
    """Add specific route /hbnb"""
    return 'HBNB!'
@app.route('/c/<text>')
def c_text(text):
    return 'C' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def is_number(n):
    return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('6-number_odd_or_even.html', n=n)

@app.route('/number_odd_or_even/<int:n>' strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

