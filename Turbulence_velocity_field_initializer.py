
# coding: utf-8

# In[1]:

import pyximport; pyximport.install()
import numpy as np
import h5py
import time
import turbulence

def run_generator(N = 256, index=3.0/2.0, seed=0x4d3d3d3,
                  output_fn = "vel_init",binary=False):
    vel2 = turbulence.Turbulence_Generator((N,N,N),
             index, 1, N**3, [0.0,0.0,0.0], [1.0/N, 1.0/N, 1.0/N],
             seed)
    if binary:
        vel2.tofile(output_fn)

    h=h5py.File(output_fn,'w')
    h.create_dataset('dataset_1',data=vel2)
    h.close()
