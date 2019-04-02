cimport cython
import numpy as np
cimport numpy as np
cimport libc.math as cmath

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Density_Generator(_dims,index,kmin,kmax, seed,mu=1.0,sigma=0.1):
    cdef np.ndarray[np.float64_t, ndim=3] k_wave, kxs, kys, kzs, phase, gauss_amp, ds, density
    cdef np.ndarray[np.float64_t, ndim=1] kx, ky, kz
    #cdef np.ndarray[np.complex128_t, ndim=3] density
    cdef int dims[3]
    dims[0] = _dims[0]
    dims[1] = _dims[1]
    dims[2] = _dims[2]
    '''
    kx=np.fft.fftfreq(dims[0], d=1.0/dims[0])
    ky=np.fft.fftfreq(dims[1], d=1.0/dims[1])
    kz=np.fft.fftfreq(dims[2], d=1.0/dims[2])

    kx[0]=kx[1]*1.0e-10
    ky[0]=ky[1]*1.0e-10
    kz[0]=kz[1]*1.0e-10
    '''
    kx=np.mgrid[kmin:kmax:1j * dims[0]]
    ky=np.mgrid[kmin:kmax:1j * dims[1]]
    kz=np.mgrid[kmin:kmax:1j * dims[2]]

    rand=np.random.RandomState(seed)

    #phase=rand.rand(dims[0],dims[1],dims[2])*np.pi*2
    #gauss_amp=rand.rand(dims[0],dims[1],dims[2])

    kxs, kys, kzs = np.meshgrid(kx,ky,kz)

    k_wave=np.sqrt(kxs*kxs+kys*kys+kzs*kzs)
    density = rand.normal((k_wave)**(-0.5*index-1)) #* np.exp(phase*1j) * gauss_amp
    #density[k_wave < kmin] = 0.0

    ds=np.fft.ifftn(density).real
    
    #density = rand.lognormal((k_wave)**(-0.5*index-1))

    #density= rand.lognormal(mu,sigma,size=(dims[0],dims[1],dims[2]))
    
    #ds= (np.fft.ifftn(density).real)
    #ds=density-1.01*density.min()

    return ds
