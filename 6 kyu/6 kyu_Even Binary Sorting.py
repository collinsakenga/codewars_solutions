def even_binary(n):
    res=[int(i, 2) for i in n.split()]
    index=0
    even=sorted([i for i in res if i%2==0])
    for i,j in enumerate(res):
        if j%2==0:
            res[i]=even[index]
            index+=1
    return " ".join(bin(i)[2:].rjust(3, "0") for i in res)