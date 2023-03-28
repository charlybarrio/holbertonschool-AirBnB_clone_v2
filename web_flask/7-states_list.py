#!/usr/bin/python3
""" Task 7 module """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns a sorted list of states"""
    states = storage.all(states).values()
    states_sorted = sorted(states, key=lambda state: state.name)

    return render_template('7-states_list.html', states_list=states_sorted)


@ app.teardown_appcontext
def closing(dummy):
    """closes alchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
