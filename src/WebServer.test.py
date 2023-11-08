from WebServer import WebServer
from Plotter import Plotter

class Test_plotter():
    def __init__(self,image_path):
        self.img_path = image_path

    def plot(self):
        return self.img_path

data = [1, 2, 3, 4, 5]
output_file = "grafico.png"

if __name__ == '__main__':
    ws = WebServer()
    plotter = Plotter()
    image_path = plotter.plot_and_save_data(data, output_file)
    #ws.add_route_execute('/images/img_1')
    print(f"Imagem salva em {image_path}")
    ws.run_server()