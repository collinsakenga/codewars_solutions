def cut_log(p, n):
    maximum=[0]
    for j in range(1, n+1):
        comp=-float("inf")
        for i in range(1, j+1): # Two nested loops = Θ(n^2)
            comp=max(p[i-1+1]+maximum[j-i], comp)
        maximum.append(comp)
    return maximum[-1]