import numpy as np
import random as rand
cimport numpy as np

def simulacion_ising(int N, double T, int t):
    cdef int a, b, c, d, i, j, k, l, n, m, x
    cdef double DE, pi, pr, e
    cdef np.ndarray s, m_N, E_S, E_S2, fi, f_val
    cdef double mN, ES, ES2, eN, cN
    cdef int jl
    
    def DeltaE(np.ndarray[np.float64_t, ndim=2] s, int n, int m, int N):
        cdef int a, b, c, d
        
        if n == N - 1:
            a = 1
            b = N - 2
        elif n == 0:
            a = 1
            b = N - 2
        else:
            a = n + 1
            b = n - 1
        
        if m == N - 1:
            c = 1
            d = N - 2
        elif m == 0:
            c = 1
            d = N - 2
        else:
            c = m + 1
            d = m - 1
        
        DE = 2 * s[n, m] * (s[a, m] + s[b, m] + s[n, c] + s[n, d])
        return DE

    def p(double DE, double T):
        cdef double pi
        
        pi = np.exp(-DE / T)
        if pi < 1:
            p = pi
        else:
            p = 1
        return p

    s = np.ones((N, N), dtype=np.float64)
    m_N = np.zeros(t, dtype=np.float64)
    E_S = np.zeros(t, dtype=np.float64)
    E_S2 = np.zeros(t, dtype=np.float64)
    fi = np.zeros((N - 1, N, N), dtype=np.float64)
    x = 0

    for i in range(t):
        if i % 100 == 0:
            x += 1
            m = 0
            Es = 0  
            for j in range(N):
                for k in range(N):
                    m += s[j, k]
                    Es -= DeltaE(s, j, k, N)
                    for l in range(1, N):
                        if j + l > N - 1:
                            jl = j + l - N
                        else:
                            jl = j + l
                        fi[l - 1, j, k] += s[j, k] * s[jl, k]

            m_N[i] = abs(m / (N ** 2))
            E_S[i] = Es / 4
            E_S2[i] = (Es / 4) ** 2

        for _ in range(N**2):
            n = rand.randrange(0, N)
            m = rand.randrange(0, N)
            
            DE = DeltaE(s, n, m, N)
            pr = p(DE, T)
            e = rand.uniform(0, 1)
            
            if e < pr:
                s[n, m] = -s[n, m]

    mN = np.sum(m_N) / x
    ES = np.sum(E_S) / x
    ES2 = np.sum(E_S2) / x

    eN = ES / (2 * N)
    cN = (ES2 - ES ** 2) / (T * N ** 2)

    fi /= (x * N ** 2)
    f_val = np.zeros(N - 1, dtype=np.float64)

    for i in range(N - 1):
        f_val[i] = np.sum(np.sum(fi[i]))

    return mN, eN, cN, f_val
