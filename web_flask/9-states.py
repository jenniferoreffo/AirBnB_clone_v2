#!/usr/bin/bash
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from operator import attrgetter

app = Flask(__name__)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects sorted by name."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=attrgetter('name'))
    return render_template('9-states.html', sorted_states=sorted_states)

app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
     """Displays a HTML page with cities linked to a specific State"""
     state = storage.get(State, id)
     if state:
         cities = sorted(state.cities, key=attrgetter('name')) if hasattr(state, 'cities') else state.cities()
         return render_template('9-states.html', state=state, cities=cities)
     else:
         return render_template('9-states.html', not_found=True)
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
