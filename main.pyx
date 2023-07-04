import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def calculate_values(np.ndarray[np.float64_t, ndim=3] g, int N, int P):
    # Variable a
    cdef np.ndarray[np.float64_t, ndim=1] a = np.zeros(P)
    cdef int num, i, j

    for num in range(P):
        for i in range(N):
            for j in range(N):
                a[num] += g[num, i, j]

    a /= (N**2)

    # Peso sináptico w
    cdef np.ndarray[np.float64_t, ndim=4] w = np.zeros([N, N, N, N])
    cdef int i, j, k, l

    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if (i, j) == (k, l):
                        continue
                    else:
                        for num in range(P):
                            w[i, j, k, l] += (g[num, i, j] - a[num]) * (g[num, k, l] - a[num]) / (N**2)

    # Umbral de disparo
    cdef np.ndarray[np.float64_t, ndim=2] O = np.zeros([N, N])
    cdef int i, j, k, l

    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    O[i, j] += w[i, j, k, l]

    O /= 2

    return a, w, O

