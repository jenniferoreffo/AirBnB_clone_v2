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

@app.route('/c/<string:text>', strict_slashes=False)
def hello():
    """Display c followed by the value of text, replace "_" with " "  """
    return "c{}".format(text.replace('_',' '))
    
@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text='is_cool'):
    """inputed text, replace "_" with " " """
    return "python {}".format(text.replace('_',' '))

@app_.route('/number/<int:n>', strict_slashes=False)
def number(n=None):
    """Dynamic inputed interger"""
    return "%d is a number" % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def first_template(n=None):
    """Display HTMI page only if n is and integer"""
    return render_template('5-number.html', n=n)

@app.route('/number_odd_even/<int:n>', strict_slashes=False)
def cond_template(n=None):
    """Display a HTML page only if n is an integer odd or even"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

