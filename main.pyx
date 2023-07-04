import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def calculate_values(np.ndarray[np.float64_t, ndim=3] g, int N, int P):
    # Variable a
    cdef np.ndarray[np.float64_t, ndim=1] a = np.zeros(P)
    cdef int num, x, y

    for num in range(P):
        for x in range(N):
            for y in range(N):
                a[num] += g[num, x, y]

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
                        for n in range(P):
                            w[i, j, k, l] += (g[n, i, j] - a[n]) * (g[n, k, l] - a[n]) / (N**2)

    # Umbral de disparo
    cdef np.ndarray[np.float64_t, ndim=2] O = np.zeros([N, N])
    cdef int r, s, t, u

    for r in range(N):
        for s in range(N):
            for t in range(N):
                for u in range(N):
                    O[r, s] += w[r, s, t, u]

    O /= 2

    return a, w, O

