#!/usr/bin/python3
"""
Flask web application
* web application is listening on 0.0.0.0, port 5000
* Routes:
      * /: display Hello HBNB!
* Option strict_slashes=False
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Starts a Flask web application.

    Exporting environment variable:
       FLASK_APP=0-hello_route.py
       FLASK_ENV=development
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def dis_hbnb():
    """
    Starts a Flask web application.
    Exporting environment variable:
       FLASK_APP=0-hello_route.py
       FLASK_ENV=development
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
