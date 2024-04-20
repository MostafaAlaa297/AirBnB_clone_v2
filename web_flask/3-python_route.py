#!/usr/bin/python3

"""
Starts a flask app
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def python_hello():
	"""displays Hello HBNB"""
	return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def python_hbnb():
        """displays Hello HBNB"""
        return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def python_C(text):
	"""displays c followed text"""
	text = text.replace("_", " ")
	return 'C {}'.format(str(text))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
        """displays python followed by text"""
        text = text.replace("_", " ")
        return 'Python {}'.format(text)



if __name__ ==  '__main__':
	app.run(host='0.0.0.0', port='5000')
