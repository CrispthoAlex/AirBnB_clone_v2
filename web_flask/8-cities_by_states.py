#!/usr/bin/python3
"""
Flask web application
* web application is listening on 0.0.0.0, port 5000
* Routes:
      * /: display Hello HBNB!
* Option strict_slashes=False
* Tell to terminal the application, exporting the FLASK_APP
    environment variable:
    FLASK_APP="filename"
    FLASK_ENV=development
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a HTML page with a list of States objects """
    return render_template('7-states_list.html',
                           list_states=storage.all(State).values())


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ Display a HTML page with a list of Cities objects """
    return render_template('8-cities_by_states.html',
                           list_states=storage.all(State).values())


@app.teardown_appcontext
def teardown_db(db):
    """
    Method to remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
