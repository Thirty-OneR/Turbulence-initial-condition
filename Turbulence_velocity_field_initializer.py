
# coding: utf-8

# In[1]:


import numpy as np
import h5py
import time
get_ipython().run_line_magic('load_ext', 'cython')


# In[2]:


get_ipython().run_cell_magic('cython', '', '\ncimport cython\nimport numpy as np\ncimport numpy as np\ncimport libc.math as cmath\n\n@cython.boundscheck(False)\n@cython.wraparound(False)\n@cython.cdivision(True)\ndef Turbulence_Generator(_dims, index, kmin, kmax, leftedge, cellwidth, seed):\n    cdef np.ndarray[np.float64_t, ndim=4] vel\n    cdef np.ndarray[np.float64_t, ndim=1] kxs, kys, kzs\n    cdef np.ndarray[np.float64_t, ndim=3] Ax, Ay, Az, AA, k_wave, Ak0, vs, k2\n    cdef int dims[3]\n    dims[0] = _dims[0]\n    dims[1] = _dims[1]\n    dims[2] = _dims[2]\n    \n    vel = np.zeros([3, dims[0], dims[1], dims[2]])\n\n    rand=np.random.RandomState(seed)\n\n    kxs = np.mgrid[kmin:kmax:1j * dims[0]]\n    kys = np.mgrid[kmin:kmax:1j * dims[1]]\n    kzs = np.mgrid[kmin:kmax:1j * dims[2]]\n    \n    k2 = ((kxs*kxs)[:,None,None]\n        + (kys*kys)[None,:,None]\n        + (kzs*kzs)[None,None,:])\n    \n    Ax = rand.rand(dims[0], dims[1], dims[2])\n    Ay = rand.rand(dims[0], dims[1], dims[2])\n    Az = rand.rand(dims[0], dims[1], dims[2])\n    AA = np.sqrt(Ax**2 + Ay**2 + Az**2)\n    Ax /= AA\n    Ay /= AA\n    Az /= AA\n\n    k_wave=np.sqrt(k2)\n    Ak0 = rand.normal((k_wave)**(-0.5*index-1))  # Probably need to specify "scale"\n    \n    cdef np.float64_t pi = np.pi\n    \n    vs= (np.fft.ifftn(Ak0).real)\n    \n    vel[0,:,:,:]= Ax*vs\n    vel[1,:,:,:]= Ay*vs\n    vel[2,:,:,:]= Az*vs\n                    \n    return vel')


# In[ ]:


N=64
index=3/2
seed=0x4d3d3d3
    
vel2= Turbulence_Generator((N,N,N), index, 1, N**3, [0.0,0.0,0.0],[1.0/N, 1.0/N, 1.0/N], seed)
vel2.tofile('vel_init')

