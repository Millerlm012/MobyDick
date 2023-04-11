import unittest
import requests

class TestAPIMethods(unittest.TestCase):

    def test_get_top_100(self):
        req = requests.get('http://host.docker.internal/api/top_100')

        self.assertEqual(200, req.status_code)
        self.assertEqual(100, len(req.json()))

if __name__ == '__main__':
    unittest.main()