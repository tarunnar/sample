import webapp2
import unittest
import json
from main import app


class TestHelloWebapp2(unittest.TestCase):
    def test_sample(self):
        req = webapp2.Request.blank("/")
        response = req.get_response(app)
        print (dir(response))
        print (response.http_status_message(response.status_int))
        print (response.headers)
        self.assertEqual(
            json.dumps({
                "data": "data"
            }), response.body
        )
        self.assertEqual(404, response.status_int)
