#!/usr/bin/python3

"""
Starts a flask app
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def temp_hello():
	"""displays Hello HBNB"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def temp_hbnb():
        """displays Hello HBNB"""
        return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def temp_C(text):
	"""displays c followed text"""
	text = text.replace("_", " ")
	return 'C {}'.format(str(text))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def temp_python_is_cool(text):
        """displays python followed by text"""
        text = text.replace("_", " ")
        return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def temp_n(n):
        """displays python followed by text"""
        return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def temp(n):
        """displays n in html"""
        return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def temp_even_or_odd(n):
        """displays n in html"""
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ ==  '__main__':
	app.run(host='0.0.0.0', port='5000')
