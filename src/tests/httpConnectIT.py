import unittest
import requests

class httpConnectIT(unittest.TestCase):

    # https://kevinmccarthy.org/2014/08/03/integration-testing-flask-apps/

    def http_request_tasks(server):
        assert requests.get(server + '/duck').status_code == 404
        assert requests.get(server + '/').status_code == 200

if __name__ == '__main__':
    unittest.main()