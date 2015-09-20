import matplotlib.pylab as plt
import numpy as np
import pandas as pd


def plot_spectrum(xdata, ydata, **kwargs):
    '''
    Plots the spectrum
    '''
    fig, ax = plt.subplots()
    ax.plot(xdata, ydata, **kwargs)
    return fig
