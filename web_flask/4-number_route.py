#!/usr/bin/python3

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
    """returns given text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show(text='is cool'):
    """return python is cool or given text"""
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns number if int"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
