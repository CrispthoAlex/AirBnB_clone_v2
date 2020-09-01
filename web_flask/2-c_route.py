#!/usr/bin/python3
"""
Flask web application
* web application is listening on 0.0.0.0, port 5000
* Routes:
      * /: display Hello HBNB!
* Option strict_slashes=False

Exporting environment variable:
   FLASK_APP=0-hello_route.py
   FLASK_ENV=development
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
    Starts a Flask web application.
    disply Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def dis_hbnb():
    """
    Starts a Flask web application.
    display HBNB
    """
    return 'HBNB'


@app.route('/c/<text>')
def dis_c_text(text):
    """
    Starts a Flask web application.
    display C "text"
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
