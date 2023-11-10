class WebServer:
    
    def __init__(self, Flask, send_file, request, plotter):
        """
        @brief This is the constructor for the WebServer class.
        @param Flask This is an instance of the Flask class. By default, it's initialized with the name of the current module.
        @param port This is the port number on which the server will run. By default, it's set to 8080.
        @return It returns a WebServer object.
        """
        self.__Flask = Flask
        self.__port = 8080
        self.__send_file = send_file
        self.__httpRequest = request
        self.__plotter= plotter
        
    def add_route_execute(self, route):
        """
        @brief This method adds a new route to the Flask application and associates it with a function that sends a file as a response.
        @param route This is the URL rule as a string.
        @param plotter This is an object that has a plot method which returns the path to the image file to be sent as a response.
        """
        def route_handler():
            data = self.__httpRequest.args.get('data', -1)
            try:
                data = data.strip('[').strip(']').split(',')
                data = [float(x) for x in data]
            except:
                data = -1
            plot_path = self.__plotter.plot(data, 'plot')
            return self.__send_file(plot_path)

        self.__Flask.add_url_rule(route, route, route_handler)
        
    def run_server(self):
        """
        @brief This method starts the Flask web server.
        @return None.
        """
        self.__Flask.run(debug=False, port=self.__port)
    
    def getFlask(self):
        return self.__Flask