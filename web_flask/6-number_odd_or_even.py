#!/usr/bin/python3

from flask import Flask, render_template

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
    """returns default text or give text"""
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns input if number"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_number(n):
    """returns number in html template"""
    return render_template('5-number.html')


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """returns html template with odd or even text"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
