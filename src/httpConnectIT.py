import appContainer
import unittest
from mongo_dao import DbConnector
from pymongo import MongoClient

class httpConnectIT(unittest.TestCase):

    def setUp(self):
        self.appTestClient = appContainer.app.test_client()
        self.client = MongoClient('0.0.0.0', 27017)
        self.client.duck_db.duckCounter.drop()
        appContainer.db = DbConnector()


    def test_flask_application_is_up_and_running(self):
        result = self.appTestClient.get('/duck')
        self.assertEqual(result.data, "Current duck count : 0 ducks.")

        result = self.appTestClient.put('/duck')
        self.assertEqual(result.data, "Increased duck count by one.")
        state = self.client.duck_db.duckCounter.find_one({'_id': 1}, {'counter' : 1})['counter']
        dbResult = self.client.duck_db.duckCounter.find_one({'_id': 1}, {'counter': 1})
        self.assertEqual(dbResult['counter'], 1)

        self.appTestClient.put('/duck')
        self.appTestClient.put('/duck')
        result = self.appTestClient.get('/duck')
        self.assertEqual(result.data, "Current duck count : 3 ducks.")
        dbResult = self.client.duck_db.duckCounter.find_one({'_id': 1}, {'counter': 1})
        self.assertEqual(dbResult['counter'], 3)

        result = self.appTestClient.delete('/duck')
        self.assertEqual(result.data, "Decreased duck count by one.")


        result = self.appTestClient.post('/duck')
        self.assertEqual(result.data, "Duck counts resetted to 0!")
        dbResult = self.client.duck_db.duckCounter.find_one({'_id': 1}, {'counter': 1})
        self.assertEqual(dbResult['counter'], 0)


        result = self.appTestClient.get('/duck')
        self.assertEqual(result.data, "Current duck count : 0 ducks.")

if __name__ == '__main__':
    unittest.main()