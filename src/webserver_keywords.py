from WebServer import WebServer
# from flask import Flask, send_file, request

def GetWebServerInstance(Flask, sendFile, request, plotter):
    return WebServer(Flask, sendFile, request, plotter)

def GetFlaskInstanceFromWebServer(webserver: WebServer):
    return webserver.getFlask()

def ExecuteWebServerRouterHandler(webserver: WebServer):

    return

class PlotterMock:
    def plot():
        return '1'

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

def getPlotterMock():
    return PlotterMock()

def requestMock():
    return MockRequestArgs()

def mock():
    return 'mock'

def sendFileMock():
    return 'send'


class MockRequest:
    def __init__(self, args):
        self.args = args

    def get(self, key, default=None):
        return self.args.get(key, default)