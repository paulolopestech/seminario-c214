import matplotlib.pyplot as plt
import seaborn as sb

class Plotter:
    
    def _init_(self):        
        pass

    @staticmethod
    def plot(data):
        output_directory = './buffer'
        if data  == -1:
            plt.legend(loc='center')
            plt.plot(1, label='ERRO')
            plt.savefig('buffer/erro_plot.png', format='png')
            output_file = output_directory + 'data_plot.png'
        else:
            plt.legend(loc='center')
            plt.plot(data)
            output_file = 'buffer/data_plot.png'
            plt.savefig('buffer/data_plot.png', format='png')
            output_file = output_directory + 'data_plot.png'
            plt.close()

        return output_file