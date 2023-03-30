#!/usr/bin/python3
"""task 8"""i

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """print state and cities"""
    states_dict = storage.all(State).values()
    states_city_dict = {}

    for state in states_dict:
        states_city_dict[state] = state.cities

    return render_template('7-states_list.html',
                           states_city_dict=states_city_dict)
