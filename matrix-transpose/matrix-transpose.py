import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    r = len(A)
    c = len(A[0])
    t = np.zeros((c, r))
    for i in range(r):
        for j in range(c):
            t[j][i]= A[i][j]
    return t