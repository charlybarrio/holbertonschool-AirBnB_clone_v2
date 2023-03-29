#!/usr/bin/python3
""" Task 2 module """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """returns text"""
    return "C" + " " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
