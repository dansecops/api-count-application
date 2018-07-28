from mongo_dao import DbConnector
from pymongo import MongoClient
import unittest

class DbConnectorIntegrationTest(unittest.TestCase):

    def test_creates_0_value(self):
        client = MongoClient('0.0.0.0', 27017)
        client.duck_db.duckCounter.drop()
        ccc
        result = client.duck_db.duckCounter.find_one({'_id': 1})
        self.assertEqual(result, {'_id': 1, 'counter' : 0})

    def test_uses_existing_value(self):
        client = MongoClient('0.0.0.0', 27017)
        client.duck_db.duckCounter.drop()
        client.duck_db.duckCounter.insert({'_id': 1, 'counter' : 42})
        DbConnector()
        result = client.duck_db.duckCounter.find_one({'_id': 1})
        self.assertEqual(result, {'_id': 1, 'counter': 42})


if __name__ == '__main__':
    unittest.main()