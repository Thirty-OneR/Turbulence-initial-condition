cimport cython
import numpy as np
cimport numpy as np
cimport libc.math as cmath

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Density_Generator(_dims,index,kmin,kmax, seed,mu=1.0,sigma=0.1):
    cdef np.ndarray[np.float64_t, ndim=3] density, ds, k_wave, k2
    cdef np.ndarray[np.float64_t, ndim=1] kxs, kys, kzs
    cdef int dims[3]
    dims[0] = _dims[0]
    dims[1] = _dims[1]
    dims[2] = _dims[2]
    
    rand=np.random.RandomState(seed)

    kxs = np.mgrid[kmin:kmax:1j * dims[0]]
    kys = np.mgrid[kmin:kmax:1j * dims[1]]
    kzs = np.mgrid[kmin:kmax:1j * dims[2]]

    k2 = ((kxs*kxs)[:,None,None]
        + (kys*kys)[None,:,None]
        + (kzs*kzs)[None,None,:])

    k_wave=np.sqrt(k2)
    density = rand.lognormal((k_wave)**(-0.5*index-1))

    #density= rand.lognormal(mu,sigma,size=(dims[0],dims[1],dims[2]))
    
    ds= (np.fft.ifftn(density).real)
    #ds=density-1.01*density.min()

    return ds
