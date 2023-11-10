from WebServer import WebServer

def GetWebServerInstance(flask, port=8080, request= None):
    return WebServer(flask, port=8080, request=None)

def GetFlaskInstanceFromWebServer(webserver: WebServer):
    return webserver.getFlask()

class FlaskMock:
    def __init__(self) -> None:
        pass

    def run():
        return 'running flask'

    def addRule():
        return 'add rule'

def GetFlaskMockInstance():
    flaskMock = FlaskMock()
    return flaskMock

class MockRequestArgs:
    def __init__(self, data_value=-1):
        self.data_value = data_value

    def get(self, key, default=None):
        if key == 'data':
            return self.data_value
        return default

def requestMock():
    return MockRequestArgs()

def mock():
    return 'mock'


class MockRequest:
    def __init__(self, args):
        self.args = args

    def get(self, key, default=None):
        return self.args.get(key, default)