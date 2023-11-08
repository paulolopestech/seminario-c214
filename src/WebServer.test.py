from WebServer import WebServer
from Plotter import Plotter
   
if __name__ == '__main__':
    plotter = Plotter()
    ws = WebServer()
    ws.add_route_execute('/images/', plotter)
    ws.run_server()