from flask import Flask
from random import choice

app = Flask(__name__)

names = [
	'abominations',
	'brigands',
	'chumps',
	'dorks',
	'enemies',
	'foolish mortals',
	'goobers',
	'hobgoblins',
	'idiots',
	'jerks',
	'killjoys',
	'lollygaggers',
	'meatbags',
	'nerds',
	'oafs',
	'punks',
	'quacks',
	'rustbuckets',
	'stooges',
	'twerps',
	'unwashed masses',
	'villains',
	'worms',
	'xenomorphs',
	'yuppies',
	'zombies'
]

@app.route('/')
def hey():
	greeting = 'Hey {}!\n'.format(choice(names))
	return greeting
