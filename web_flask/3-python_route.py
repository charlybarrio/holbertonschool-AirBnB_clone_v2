#!/usr/bin/python3
""" Task 3 module """

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


@app.route('/c/<text>', strict_slashes=False)
def string(text):
    """returns text"""
    text = text.replace("_", " ")
    return "C" + " " + text


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """return text"""
    return f"Python {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
