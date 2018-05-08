#import pymysql

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from models.planet import Planet

app = Flask(__name__)

Planet = Planet()

@app.route('/planets/store', methods=['POST'])
def store():
	try:
		Planet.setName(request.form['name'])
		Planet.setWeather(request.form['weather'])
		Planet.setTerrain(request.form['terrain'])
		data = Planet.store()
		return formatResponse(data)
	except Exception as ex:
		return formatResponse(ex, False)

@app.route('/planets/getAll/<skip>/<limit>')
def getAll(skip, limit):
	try:
		data = Planet.getAll(skip, limit)
		return formatResponse(data)
	except Exception as ex:
		return formatResponse(ex, False)

@app.route('/planets/getByName/<name>')
def getPlanetsByName(name):
	try:
		Planet.setName(name)
		data = Planet.getByName()
		return formatResponse(data)
	except Exception as ex:
		return formatResponse(ex, False)

@app.route('/planets/getById/<id>')
def getPlanetById(id):
	try:
		Planet.setId(id)
		data = Planet.getById()
		return formatResponse(data)
	except Exception as ex:
		return formatResponse(ex, False)

@app.route('/planets/remove/<id>')
def removePlanet(id):
	try:
		Planet.setId(id)
		data = Planet.remove()
		return formatResponse(data)
	except Exception as ex:
		return formatResponse(ex, False)

def formatResponse(data, success = True):
	response = {
		'success' : success,
		'response' : data
	}
	return jsonify(str(response))

if __name__ == '__main__':
     app.run(port='5002')