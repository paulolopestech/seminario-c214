from flask import Flask, send_file, request

class WebServer:
    
    def __init__(self, Flask=Flask(__name__), port=8080):
        """
        @brief This is the constructor for the WebServer class.
        @param Flask This is an instance of the Flask class. By default, it's initialized with the name of the current module.
        @param port This is the port number on which the server will run. By default, it's set to 8080.
        @return It returns a WebServer object.
        """
        self.__Flask = Flask
        self.__port = port
        
    def add_route_execute(self, route, plotter):
        """
        @brief This method adds a new route to the Flask application and associates it with a function that sends a file as a response.
        @param route This is the URL rule as a string.
        @param plotter This is an object that has a plot method which returns the path to the image file to be sent as a response.
        """
        def route_handler():
            data = request.args.get('data', -1)
            try:
                data = data.strip('[').strip(']').split(',')
                data = [float(x) for x in data]
            except:
                data = -1
            
            plot_path = plotter.plot(data)
            return send_file(plot_path)
        
        self.__Flask.add_url_rule(route, route, route_handler)
        
    def run_server(self):
        """
        @brief This method starts the Flask web server.
        @return None.
        """
        self.__Flask.run(debug=False, port=self.__port)
    
    def getFlask(self):
        return self.__Flask