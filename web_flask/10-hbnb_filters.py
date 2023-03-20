#!/usr/bin/python3

from flask import Flask, render_template
import operator

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Shows html file"""

    from models import storage
    from models.state import State
    from models.amenity import Amenity

    states = storage.all(State)

    new_list = []
    for value in states.values():
        new_list.append(value)

    sorted_state_list = sorted(new_list, key=operator.attrgetter('name'))

    state_city = {}
    for state in sorted_state_list:
        state_city[state] = sorted(
            state.cities, key=operator.attrgetter('name'))

    Amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.html', state_city=state_city, Amenities=Amenities)


@app.teardown_appcontext
def closing(dummy):
    """closes alchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
