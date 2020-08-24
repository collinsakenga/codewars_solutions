import numpy as np


def matrix_mult(a, b):
    a = np.array(a)
    b = np.array(b)
    result = []
    for i in a.dot(b):
        result.append(list(i))
    return result
