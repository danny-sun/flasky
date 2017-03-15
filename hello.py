from flask import Flask
from flask.ext.script import Manger

app = Flask(__name__)
manger = Manger(app) 

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, %s!</h1>' % name 

if __name__ == '__main__':
	manger.run()
