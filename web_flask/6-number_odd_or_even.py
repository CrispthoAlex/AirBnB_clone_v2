#!/usr/bin/python3
"""
Flask web application
* web application is listening on 0.0.0.0, port 5000
* Routes:
      * /: display Hello HBNB!
* Option strict_slashes=False

Exporting environment variable:
   FLASK_APP="filename"
   FLASK_ENV=development
"""
from flask import Flask, render_template
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
def dis_c_text(text=None):
    """
    Starts a Flask web application.
    display C "text"
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def dis_python_text(text='is cool'):
    """
    Starts a Flask web application.
    display Python "text"
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def dis_number(n=None):
    """
    Starts a Flask web application.
    display "n is a number"
    """
    return '{} is a number'.format(n)


@app.route('/number_template/')
@app.route('/number_template/<int:number>')
def number_temp(number=None):
    """
    Starts a Flask web application.
    display a HTML page only if n is an integer:
        H1 tag: Number: n inside the tag BODY
    """
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even')
@app.route('/number_odd_or_even/<int:n>')
def number_is(n=None):
    """
    Starts a Flask web application.
    display a HTML page only if n is an integer:
        H1 tag: Number: n inside the tag BODY
    """
    return render_template('6-number_odd_or_even.html', numberis=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
