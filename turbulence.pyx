cimport cython
import numpy as np
cimport numpy as np
cimport libc.math as cmath

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def Turbulence_Generator(_dims, index, kmin, kmax, leftedge, cellwidth, seed):
    cdef np.ndarray[np.float64_t, ndim=4] vel
    cdef np.ndarray[np.float64_t, ndim=1] kx, ky, kz
    cdef np.ndarray[np.float64_t, ndim=3] Ax, Ay, Az, AA, k_wave, kxs, kys, kzs, vs, Ak0
    #cdef np.ndarray[np.complex128_t, ndim=3] Ak0
    cdef int dims[3]
    dims[0] = _dims[0]
    dims[1] = _dims[1]
    dims[2] = _dims[2]
    
    vel = np.zeros([3, dims[0], dims[1], dims[2]])

    rand=np.random.RandomState(seed)
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

    #phase=rand.rand(dims[0],dims[1],dims[2])*np.pi*2
    #gause_amp=rand.rand(dims[0],dims[1],dims[2])

    Ax = (rand.rand(dims[0], dims[1], dims[2])-0.5)*2
    Ay = (rand.rand(dims[0], dims[1], dims[2])-0.5)*2
    Az = (rand.rand(dims[0], dims[1], dims[2])-0.5)*2
    AA = np.sqrt(Ax**2 + Ay**2 + Az**2)
    Ax /= AA
    Ay /= AA
    Az /= AA
    
    kxs, kys, kzs = np.meshgrid(kx,ky,kz)
    k_wave=np.sqrt(kxs*kxs+kys*kys+kzs*kzs)
    Ak0 = rand.normal((k_wave)**(-0.5*index-1)) #* np.exp(phase*1j) * gause_amp  # Probably need to specify "scale"
    #Ak0[k_wave < kmin] = 0.0

    vs= (np.fft.ifftn(Ak0).real)
    
    vel[0,:,:,:]= Ax*vs
    vel[1,:,:,:]= Ay*vs
    vel[2,:,:,:]= Az*vs
                    
    return vel
