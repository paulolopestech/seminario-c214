import matplotlib.pyplot as plt
import seaborn as sb
import os

class Plotter:
    
    def __init__(self):        
        pass

    def plot(self, data):

        os.makedirs(os.path.join("src", "buffer"), exist_ok=True)
        src_path = os.path.join("buffer", "data_plot.png")
        image_path = os.path.join("src", src_path)

        sb.set_style("whitegrid")
        plt.figure(figsize=(10, 5))

        if data == -1:
            plt.plot(1, label='ERRO')
            plt.legend(loc='center')
            plt.savefig(image_path, format='png')
            plt.close()
        else:
            plt.plot(data)
            plt.savefig(image_path, format='png')
            plt.close()

        return src_path