#!/usr/bin/python3
"""
A script that starts flask web app

"""
from flask import Flask

app= Flask(__name__)

@app.route("/", strict_slashes=False)

def hello():
    """Starts basic Flask web application"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    """This runs if not imported"""
    app.run(host='0.0.0.0', port=5000)
