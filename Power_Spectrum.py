import pyximport; pyximport.install()
import numpy as np
import h5py
import time
import power_spectrum

def draw_power_spectrum(N = 64, bins = 32, figname='power_specturm'):
    power_spectrum.draw_ps(N=N, bins=bins, figname=figname)

