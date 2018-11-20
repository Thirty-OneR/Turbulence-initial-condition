cimport cython
import numpy as np
cimport numpy as np
cimport libc.math as cmath

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Turbulence_Generator(_dims, index, kmin, kmax, leftedge, cellwidth, seed):
    cdef np.ndarray[np.float64_t, ndim=4] vel
    cdef np.ndarray[np.float64_t, ndim=1] kxs, kys, kzs
    cdef np.ndarray[np.float64_t, ndim=3] Ax, Ay, Az, AA, k_wave, Ak0, vs, k2
    cdef int dims[3]
    dims[0] = _dims[0]
    dims[1] = _dims[1]
    dims[2] = _dims[2]
    
    vel = np.zeros([3, dims[0], dims[1], dims[2]])

    rand=np.random.RandomState(seed)

    kxs = np.mgrid[kmin:kmax:1j * dims[0]]
    kys = np.mgrid[kmin:kmax:1j * dims[1]]
    kzs = np.mgrid[kmin:kmax:1j * dims[2]]
    
    k2 = ((kxs*kxs)[:,None,None]
        + (kys*kys)[None,:,None]
        + (kzs*kzs)[None,None,:])
    
    Ax = rand.rand(dims[0], dims[1], dims[2])
    Ay = rand.rand(dims[0], dims[1], dims[2])
    Az = rand.rand(dims[0], dims[1], dims[2])
    AA = np.sqrt(Ax**2 + Ay**2 + Az**2)
    Ax /= AA
    Ay /= AA
    Az /= AA

    k_wave=np.sqrt(k2)
    Ak0 = rand.normal((k_wave)**(-0.5*index-1))  # Probably need to specify "scale"
    
    cdef np.float64_t pi = np.pi
    
    vs= (np.fft.ifftn(Ak0).real)
    
    vel[0,:,:,:]= Ax*vs
    vel[1,:,:,:]= Ay*vs
    vel[2,:,:,:]= Az*vs
                    
    return vel
