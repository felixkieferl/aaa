import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def valors(np.ndarray[np.float64_t, ndim=3] g, int N):
    # Variable a
    cdef double a = np.sum(np.sum(np.transpose(g))) / (N**2)

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
                        w[i, j, k, l] += np.sum((g[:, i, j] - a) * (g[:, k, l] - a)) / (N**2)

    # Umbral de disparo
    cdef double O = np.sum(w) / 2

    return a, w, O
