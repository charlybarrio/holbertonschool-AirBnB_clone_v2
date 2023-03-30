#!/usr/bin/python3
"""task 8"""i

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_print():
    """prints states"""

    import operator

    states = storage.all(State)

    new_list = []
    for value in states.values():
        new_list.append(value)

    sorted_list = sorted(new_list, key=operator.attrgetter('name'))

    return render_template('7-states_list.html', states_list=sorted_list)


@ app.teardown_appcontext
def closing(dummy):
    """closes alchemy session"""

    from models import storage

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
Footer
