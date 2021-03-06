
# coding: utf-8

# In[1]:

import yt
import pyximport; pyximport.install()
import numpy as np
import h5py
import time
import density

def run_generator(N = 256,index=1.5, seed=0x4d3d3d3,mu=1.0,sigma=0.1):
    output_fn = "den_init.h5"
    den = density.Density_Generator((N,N,N),index, 1,N**3,seed,mu,sigma)
    with h5py.File("den_init.h5", 'w') as h:
        h.create_dataset('density_dataset',data=den)
