from Plotter import Plotter

def PlotterInstance(param):
    return Plotter(param)
#retorna o parametro "param" e retorna um instancia da classe Plotter

def GetPlotPath(instance: Plotter):
    return instance.initialized
#recebe uma instancia da classe "Plotter" como argumento e retorna o atributo plotPath dessa instancia.