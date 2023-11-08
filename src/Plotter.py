import matplotlib.pyplot as plt
import seaborn as sb

class Plotter:
    # receber um dado como argumento
    # plotar os dados em formato de grafico de linhas
    # salvar o grafico plotado em formato png
    # gerar imagem
    # retorna diretorio da imagem 
    
    def __init__(self):        
        pass

    def plot_and_save_data(self, data, output_file):
        if data  == -1:
            plt.legend(loc='center')
            plt.plot(1, label='ERRO')
        else:
            plt.legend(loc='center')
            plt.plot(data)
            plt.savefig(output_file)
            plt.close()

        return output_file
