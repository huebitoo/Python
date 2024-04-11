import numpy as np

def crear_trid(n, a, b, c):
    m = np.zeros((n,n), dtype=int)
    for i in range(n):
        m[i,i] = a
        if i < n-1:
            m[i, i+1] = b
            m[i+1,i] = c
    return m
A = crear_trid(30, 7, 7, 7); print(A)
