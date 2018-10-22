from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app)

from flask import jsonify

@app.route('/')
def server_test():
	return 'Server Test'

@app.route('/daily/heatmap/')
def daily_heatmap():
	file = open("GeoJSON.json","r")
	return file.read()

@app.route('/daily/<LocationID>')
def daily_location(LocationID):
	file = open("daily_" + LocationID + ".json","r")
	return file.read()
