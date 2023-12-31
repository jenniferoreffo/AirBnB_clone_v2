#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
"""Removes the current SQLAlchemy Session"""

@app.route('/hbnb_filters', strict_slashes=False)
storage.close()

def hbnb_filters():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    """Displays an HTML page with filter options for HBNB"""
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template('10-hbnb_filters.html',
            states=states,
             cities=cities,
             amenities=amenities)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
