#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)

@app.route("/", strict_slashes=False)
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = storage.all("User").values()

    return render_template("100-hbnb.html",
                           states=states,
                           places=places,
                           usesr=users,
                           amenity=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
