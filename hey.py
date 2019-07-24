from flask import Flask
from random import choice

app = Flask(__name__)

names = [
	'meatbags',
	'jerks',
	'punks',
	'rascals',
	'brigands',
	'foolish mortals'	
]

@app.route('/')
def hey():
	greeting = 'Hey {}!\n'.format(choice(names))
	return greeting
