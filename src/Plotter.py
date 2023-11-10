import matplotlib.pyplot as plt
import seaborn as sb
import os

class Plotter:    
    def __init__(self):
        pass      

    def plot(self, data, image_name = "data_plot.png"):

        os.makedirs(os.path.join("src", "buffer"), exist_ok=True)
        image_path = os.path.join("src", "buffer", image_name)
        src_rel_path = os.path.join("buffer", image_name)

        sb.set_style("whitegrid")
        plt.figure(figsize=(10, 5))

        try:
            all(isinstance(element, float) for element in data)
        except:
            raise Exception("data needs to be an array of type float")
            
        plt.plot(data)
        plt.savefig(image_path, format='png')
        plt.close()

        return src_rel_path