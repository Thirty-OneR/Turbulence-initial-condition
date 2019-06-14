
# coding: utf-8

# In[1]:

import pyximport; pyximport.install()
import numpy as np
import h5py
import time
import turbulence

def run_generator(N = 256, index=3.0/2.0, seed=0x4d3d3d3):
    vel2 = turbulence.Turbulence_Generator((N,N,N),
             index, 1/N**3, 10*N**3, [0.0,0.0,0.0], [1.0/N, 1.0/N, 1.0/N],
             seed)
    with h5py.File("vel_init.h5",'w') as h:
        h.create_dataset('velocity_dataset',data=vel2)
