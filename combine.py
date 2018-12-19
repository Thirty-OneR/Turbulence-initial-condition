import h5py
import numpy as np

with h5py.File('vel_init','r') as f:
    vel=f['/dataset_1'][:]

with h5py.File('den_init','r') as f:
    den=f['/dataset_2'][:]

v1=vel[0]
v2=vel[1]
v3=vel[2]

h=h5py.File('dataset','w')
h.create_dataset('density',data=den)
h.create_dataset('vx',data=v1)
h.create_dataset('vy',data=v2)
h.create_dataset('vz',data=v3)
h.close()
