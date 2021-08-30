def min_dot(a, b):
    a=sorted(a)
    b=sorted(b, reverse=True)
    return sum(i*j for i,j in zip(a, b))