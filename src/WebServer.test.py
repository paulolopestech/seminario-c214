from WebServer import WebServer

class Test_plotter():
    def __init__(self,image_path):
        self.img_path = image_path

    def plot(self):
        return self.img_path
    
if __name__ == '__main__':
    ws = WebServer()
    t1 = Test_plotter('buffer/img_1.png')
    t2 = Test_plotter('buffer/img_2.png')
    ws.add_route_execute('/images/img_1', t1)
    ws.add_route_execute('/images/img_1', t2)
    ws.run_server()