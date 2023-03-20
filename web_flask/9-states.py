#!/usr/bin/python3

from flask import Flask, render_template
import operator

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_print():
    """prints list of states sorted by name"""
    from models import storage
    from models.state import State

    states = storage.all(State)

    new_list = []
    for value in states.values():
        new_list.append(value)

    sorted_state_list = sorted(new_list, key=operator.attrgetter('name'))

    return render_template('9-states.html', states_list=sorted_state_list)


@app.route('/states/<id>', strict_slashes=False)
def state_id_print(id):
    """prints state and cities sorted"""

    from models import storage
    from models.state import State

    states = storage.all(State)

    new_list = []

    for value in states.values():
        if value.id == id:
            found_state = value
            city_list = found_state.cities
            return render_template('9-states.html', found_state=found_state, city_list=city_list)


@app.teardown_appcontext
def closing(dummy):
    """closes alchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
