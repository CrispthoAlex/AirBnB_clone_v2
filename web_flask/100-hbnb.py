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
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def dis_St_Am_Pla():
    """
    Display a HTML page with a list of States, cities, places objects on
    """
    ameni = storage.all(Amenity).values()
    states = storage.all(State).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', list_states=states,
                           list_ameni=ameni, list_place=places)


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
    app.run(host='0.0.0.0', port=5000, debug=True)
