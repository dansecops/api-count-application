from pymongo import MongoClient

class DbConnector:

	def __init__(self):
		self.client = MongoClient('0.0.0.0', 27017)
		self.client.duck_db.duckCounter.update({'_id': 1}, {"$setOnInsert": {'counter' : 0}}, True)

	def increase_duck_count(self):
		return self.client.duck_db.duckCounter.update({'_id':1},{"$inc" : {'counter' : 1}}, True)

	def decrease_duck_count(self):
		return self.client.duck_db.duckCounter.update({'_id':1},{"$inc" : {'counter' : -1}}, True)

	def get_duck_count(self):
		return self.client.duck_db.duckCounter.find_one({'_id': 1}, {'counter' : 1})['counter']

	def reset_duck_count(self):
		return self.client.duck_db.duckCounter.update({'_id':1},{"$set" : {'counter' : 0}}, True)