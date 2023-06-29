import cython
import numpy as np
from libc.stdlib cimport rand, RAND_MAX
from numpy cimport ndarray, int64_t

@cython.boundscheck(False)
@cython.wraparound(False)
def f(ndarray[int64_t, ndim=2] s, double T, int N, object p, object DeltaE):
    cdef int i, n, m
    cdef double DE, pr, e
    cdef double random_num
    
    for i in range(N**2):
        n = rand() % N
        m = rand() % N
        
        n = n.astype(np.int64)
        m = m.astype(np.int64)        
        
        DE = DeltaE(s, n, m, N)
        pr = p(DE, T)
        e = rand() / <double>RAND_MAX
        
        if e < pr:
            s[n, m] = -s[n, m]
    
    return s
