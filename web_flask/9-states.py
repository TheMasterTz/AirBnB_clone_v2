#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)


@app.route("/states")
@app.route("/states/<id>")
def states(id=None):
    """"display the states and cities listed in alphabetical order"""
    if id is not None:
        states = 'State.' + id
    states = storage.all("State")
    return render_template('9-states.html', states=states, states_id=id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
