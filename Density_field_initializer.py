
# coding: utf-8

# In[1]:

import pyximport; pyximport.install()
import numpy as np
import h5py
import time
import density

def run_generator(N = 256, seed=0x4d3d3d3,mu=1,sigma=0.1,
                  output_fn = "den_init",binary=False):
    den = density.Density_Generator((N,N,N),seed,mu,sigma)
    if binary:
        den.tofile(output_fn)

    h=h5py.File(output_fn,'w')
    h.create_dataset('dataset_2',data=den)
    h.close()
