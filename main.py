import webapp2
import json
from error_codes import ErrorCodes


class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        error = ErrorCodes.ErrorCodes4XX.code_4xx_000001
        response_dict = {"errors": [error.to_dict()]}
        self.response.headers.add("Content-type", "application/json")
        self.response.status_int = 400
        return self.response.write(json.dumps(response_dict))


routes = [
    ('/', HelloWebapp2),
]

app = webapp2.WSGIApplication(
    routes=routes,
    debug=True
)

if __name__ == "__main__":
    from paste import httpserver
    httpserver.serve(app, host="127.0.0.1", port=8000)
