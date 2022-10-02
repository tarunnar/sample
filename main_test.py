import webapp2
import unittest
import json

from error_codes import ErrorCodes
from main import app


class TestHelloWebapp2(unittest.TestCase):
    def test_sample(self):
        req = webapp2.Request.blank("/")
        response = req.get_response(app)
        print (dir(response))
        print (response.http_status_message(response.status_int))
        print (response.headers)
        error = ErrorCodes.ErrorCodes4XX.code_4xx_000001
        response_dict = {"errors": [error.to_dict()]}
        self.assertEqual(400, response.status_int)
        self.assertEqual(response_dict, json.loads(response.body))

