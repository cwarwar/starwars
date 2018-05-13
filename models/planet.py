from pymongo import MongoClient
import requests
from libraries.swapi import Swapi
from models.dal.basedal import BaseDal
from models.exceptions.planet import PlanetException

class Planet:

	collectionName = 'planet'

	def __init__(self, dal : BaseDal):
		self.dal = dal

	def setId(self, id):
		self.id = str(id)

	def setName(self, name):
		self.name = name

	def setWeather(self, weather):
		self.weather = weather

	def setTerrain(self, terrain):
		self.terrain = terrain

	def store(self):
		if(self.name.strip() and self.weather.strip() and self.terrain.strip()):

			swapi = Swapi('planets')
			swapi.setName(self.name)
			timesAppeared = swapi.searchQuantityTimesAppeared()

			data = {
				'name' : self.name,
				'weather' : self.weather,
				'terrain' : self.terrain,
				'timesAppeared' : timesAppeared
			}
			return self.dal.insert(data)
		return 'False'


	def getAll(self, skip, limit):
		lista = []
		for collection in self.dal.findAll(skip, limit):
			lista.append(collection)
		return lista

	def getByName(self):
		if(self.name.strip()):
			lista = []
			for collection in self.dal.find("name", self.name):
				lista.append(collection)
			return lista

	def getById(self):
		if(self.id.strip()):
			return self.dal.findById(self.id)
		return 'False'

	def remove(self):
		if(self.id.strip()):
			return self.dal.remove(self.id)
		return 'False'
			

		
