
import importresolver
import unittest
from random import randrange
from models.planet import Planet
from models.dal.mongo import Mongo

class testPlanetModel(unittest.TestCase):
	def testInsertPlanet(self):
		
		randNumber = str(randrange(0, 10000))
		name = 'name_test'+randNumber
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()

		#Buscando o planeta
		self.Planet.setId(str(storedPlanetId))
		planetData = self.Planet.getById()

		#Comparando o planeta inserido com o buscado
		self.assertEqual(storedPlanetId, planetData['_id'])
		self.assertEqual(name, planetData['name'])
		self.assertEqual(weather, planetData['weather'])
		self.assertEqual(terrain, planetData['terrain'])
		

	def testTimesPlanetAppeared(self):

		randNumber = str(randrange(0, 10000))
		name = 'Naboo'
		weather = 'weather_test'+randNumber
		terrain = 'terrain_test'+randNumber

		#Inserindo o planeta
		Dal = Mongo(Planet.collectionName)
		self.Planet = Planet(Dal)
		self.Planet.setName(name)
		self.Planet.setWeather(weather)
		self.Planet.setTerrain(terrain)
		storedPlanetId = self.Planet.store()

		#Buscando o planeta
		self.Planet.setId(str(storedPlanetId))
		planetData = self.Planet.getById()
		self.Planet.remove()

		self.assertEqual(4, planetData['timesAppeared'])


if __name__ == '__main__':
    unittest.main()