#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """returns HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def Python_is_cool(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def Is_it_a_number(n):
    """display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space)"""
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def Number_template(n):
    return render_template("5-number.html", number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')