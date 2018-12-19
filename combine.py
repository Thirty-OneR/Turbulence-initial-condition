import h5py
import numpy as np

with h5py.File('vel_init.h5','r') as f:
    vel=f['/velocity_dataset'][:]

with h5py.File('den_init.h5','r') as f:
    den=f['/density_dataset'][:]

v1=vel[0]
v2=vel[1]
v3=vel[2]

with h5py.File('dataset.h5','w') as h:
    h.create_dataset('density',data=den)
    h.create_dataset('velocity_x',data=v1)
    h.create_dataset('velocity_y',data=v2)
    h.create_dataset('velocity_z',data=v3)
