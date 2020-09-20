def duplicate(A):
    a = sorted(A)
    b = sorted(set(A))
    for i, j in enumerate(b):
        if b[i] != a[i]:
            return a[i]
