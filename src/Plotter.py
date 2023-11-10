import matplotlib.pyplot as plt
import seaborn as sb
import os

class Plotter:

    def __init__(self, initialized):
        """
        @brief This constructor initializes the Plotter object.
        @param initialized Any value to check if the object is initialized. 
        """
        self.initialized = initialized

    def plot(self, data, image_name = "data_plot.png"):
        """
        @brief This function plots the given data and saves the plot as an image.
        @param data The data to be plotted. This should be an array of floats.
        @param image_name The name of the image file where the plot will be saved. 
        Default is "data_plot.png".
        @return The relative path to the saved image.
        @exception Raises an exception if the data is not an array of floats.
        """
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