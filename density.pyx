cimport cython
import numpy as np
cimport numpy as np
cimport libc.math as cmath

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Density_Generator(_dims, seed,mu=1.0,sigma=0.1):
    cdef np.ndarray[np.float64_t, ndim=3] density, ds
    cdef int dims[3]
    dims[0] = _dims[0]
    dims[1] = _dims[1]
    dims[2] = _dims[2]
    
    rand=np.random.RandomState(seed)

    density= rand.lognormal(mu,sigma,size=(dims[0],dims[1],dims[2]))
    
    ds= (np.fft.ifftn(density).real)
    
    return ds
