from Plotter import Plotter

def PlotterInstance(param):
    return Plotter(param)

def GetPlotPath(instance: Plotter):
    return instance.initialized