from WebServer import WebServer
# from flask import Flask, send_file, request

def GetWebServerInstance(Flask, sendFile, request, plotter):
    return WebServer(Flask, sendFile, request, plotter) # retorna a instancia da classe webserver na porta 8080 e objeto de requisição none

def GetFlaskInstanceFromWebServer(webserver: WebServer):
    return webserver.getFlask() #recebe uma instancia do webserver como argumento e retorna a instancia do flask associada a ela

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
    return flaskMock # a classe faz uma simulação com os metodos run e add rule com strings especificas e retorna a instancia da classe

class MockRequestArgs: # simula os argumentos da requisição, possuindo um método get.
    def __init__(self, data_value=-1):
        self.data_value = data_value

    def get(self, key, default=None):
        if key == 'data':
            return self.data_value
        return default

def getPlotterMock():
    return PlotterMock()

def requestMock():
    return MockRequestArgs() #retorna a instancia da classe

def mock():
    return 'mock' #retorna a string.

def sendFileMock():
    return 'send'


class MockRequest:
    def __init__(self, args):
        self.args = args

    def get(self, key, default=None):
        return self.args.get(key, default)

    #simula representando uma requisição, com um método get.