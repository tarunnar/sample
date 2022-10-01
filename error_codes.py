class Error(object):
    def __init__(self, code, title, traceback_id, message, extras=dict()):
        self.code = code
        self.title = title
        self.traceback_id = traceback_id
        self.message = message
        self.extras = extras

    def to_dict(self):
        return self.__dict__


class ErrorCodes(object):
    class ErrorCodes4XX(object):
        code_4xx_000001 = Error(
            "code_1xx_000001",
            "Field Not provided",
            "12152125267",
            "Please provide your date_of_birth"
        )
        code_4xx_000002 = Error(
            "code_1xx_000002",
            "Authentication Failure",
            "12152125267",
            "Please provide auth token"
        )
