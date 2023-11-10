from WebServer import WebServer
from Plotter import Plotter
from flask import Flask, send_file, request


if __name__ == '__main__':
    plotter = Plotter()
    ws = WebServer(Flask(__name__), send_file, request, Plotter)
    ws.add_route_execute('/plot/line/')
    ws.run_server()