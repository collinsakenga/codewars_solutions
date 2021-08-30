def vector_affinity(a, b):
    if a==b:
        return 1.0
    down=max(len(a), len(b))
    up=0
    for i in range(min(len(a), len(b))):
        if a[i]==b[i]:
            up+=1
    return up/down