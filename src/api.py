from WebServer import WebServer
from Plotter import Plotter
from flask import Flask, send_file, request


if __name__ == '__main__':
    plotter = Plotter()
    ws = WebServer(request, Flask(__name__))
    ws.add_route_execute('/plot/line/', plotter)
    ws.run_server()