from flask import Flask
from mongo_dao import DbConnector

app = Flask(__name__)
db = DbConnector()
uri = '/duck'

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route(uri, methods=['GET'])
def get_duck_count():
	return "Current duck count : " + str(db.get_duck_count()) + " ducks." 

@app.route(uri, methods=['PUT'])
def increase_duck_count():
	db.increase_duck_count()
	return "Increased duck count by one."

@app.route(uri, methods=['DELETE'])
def decrease_duck_count():
	if(db.get_duck_count() > 0):
		db.decrease_duck_count()
	return "Decreased duck count by one."

@app.route(uri, methods=['POST'])
def reset_duck_count():
	db.reset_duck_count()
	return "Duck counts resetted to 0!"