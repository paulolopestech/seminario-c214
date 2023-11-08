import matplotlib.pyplot as plt
import seaborn as sb

class Plotter:
    
    def _init_(self):        
        pass

    def plot(self, data):
        output_file = 'file.png'
        if data  == -1:
            plt.legend(loc='center')
            plt.plot(1, label='ERRO')
            plt.savefig('buffer/erro_plot.png', format='png')
        else:
            plt.legend(loc='center')
            plt.plot(data)
            output_file = 'buffer/data_plot.png'
            plt.savefig(output_file, format='png')
            plt.close()

        return output_file