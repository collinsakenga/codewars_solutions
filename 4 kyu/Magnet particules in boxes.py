def doubles(maxk, maxn):
    total=0.0
    up=1
    down=2
    temp=[]
    for j in range(1,maxn+1):
        temp.append(1/(j+1))
    for i in range(1,maxk+1):
        for j in range(1,maxn+1):
            total+=(1/i*(temp[j-1])**(2*i))
    return total