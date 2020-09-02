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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_cities(id=None):
    """ Display a HTML page with a list of States objects """
    states = storage.all(State).values()

    if id is not None:
        count_id = 0
        for sta in states:
            if id == sta.id:
                break
            count_id += 1
        if count_id >= len(states):
            id = "Not found"

    return render_template('9-states.html', list_states=states, id_state=id)


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
