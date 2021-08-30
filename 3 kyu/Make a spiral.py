def spiralize(size):
    temp = [[0]*size for _ in range(size)]
    left=0
    right=len(temp)-1
    down=len(temp)-1
    up=0
    while True:
        for i in range(left,right+1):
            if i<len(temp)-1:               
                if temp[up][i+1]==1:
                    break
            temp[up][i]=1
        up+=1    
        if temp[up+1][right]==1:
            return temp
        for i in range(up,down+1):
            if i<len(temp)-1:
                if temp[i+1][right]==1:
                    break
            temp[i][right]=1
        right-=1
        if temp[down-1][right]==1:
            return temp
        for i in range(right,left-1,-1):
            if i>0:
                if temp[down][i-1]==1:
                    break
            temp[down][i]=1
        down-=1
        if temp[down-1][right]==1:
            return temp
        if left!=0:
            left+=1
        for i in range(down,up-1,-1):
            if i>0:
                if temp[i-1][left]==1:
                    break
            temp[i][left]=1
        left+=1
        right-=1
        down-=1
        up+=1
        if temp[up+1][right]==1:
            return temp