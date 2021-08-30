def create_spiral(n):
    if not isinstance(n, int):
        return ""
    temp=[]
    for i in range(n):
        temp.append([0]*n)
    res=0
    up=0
    down=n-1
    right=n-1
    left=0
    while res<n**2:
        for i in range(left,right+1):
            res+=1
            temp[up][i]=res
        up+=1
        for i in range(up,down+1):
            res+=1
            temp[i][right]=res
        right-=1
        for i in range(right,left-1,-1):
            res+=1
            temp[down][i]=res
        down-=1
        for i in range(down,up-1,-1):
            res+=1
            temp[i][left]=res
        left+=1
    if not temp:
        return ""
    return "".join([str(i) for i in temp])