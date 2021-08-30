def common_distance(n, m, pointA, pointB):
    res=[]
    for i in range(m):
        for j in range(n):
            if ((i-pointA[1])**2+(j-pointA[0])**2)==((i-pointB[1])**2+(j-pointB[0])**2):
                res.append((j, i))
    return sorted(res, key=lambda x: (x[0], x[1]))