#!/usr/bin/bash
from flask import Flask, render_template
from models import storage
from models.state import State
from operator import attrgetter

app = Flask(__name__)

@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a HTML page with a list of all State objects sorted by name."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('cities_by_states.html', states=sorted_states)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
