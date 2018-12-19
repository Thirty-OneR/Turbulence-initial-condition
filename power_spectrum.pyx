import numpy as np
import matplotlib.pyplot as plt
import h5py

def draw_ps(N=64,bins=32,figname='power_spectrum'):
    #data=np.fromfile('vel_init')
    #data=data.reshape((3,N,N,N))
    
    with h5py.File('vel_init.h5','r') as f:
        data=f['velocity_dataset'][:]

    vx=data[0,:,:,:]
    vy=data[1,:,:,:]
    vz=data[2,:,:,:]

    E = (vx*vx)[:,:,:]+(vy*vy)[:,:,:]+(vz*vz)[:,:,:]

    ft=np.fft.fftn(E)
    power=ft.real*ft.real

    ii = (np.arange(N)[::-1])[:,None,None]
    jj = (np.arange(N)[::-1])[None,:,None]
    kk = (np.arange(N)[::-1])[None,None,:]

    kmag = ii**2 + jj**2 + kk**2

    v, b = np.histogram(kmag, bins = bins, weights = power)
    
    plt.loglog(b[:-1], v)
    plt.xlabel('scale')
    plt.ylabel('power')
    plt.savefig(figname)
