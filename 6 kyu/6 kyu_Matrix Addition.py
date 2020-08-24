def matrix_addition(a, b):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            a[i][j] += b[i][j]
    return a
