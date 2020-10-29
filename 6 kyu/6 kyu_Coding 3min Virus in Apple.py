from copy import deepcopy
def infect_apple(apple, n):
    res=deepcopy(apple)
    for _ in range(n):
        temp=deepcopy(res)
        for i in range(len(res)):
            for j in range(len(res[i])):
                if temp[i][j]!="V":
                    continue
                if i>0:
                    res[i-1][j]="V"
                if j<(len(res[i])-1):
                    res[i][j+1]="V"
                if i<(len(res)-1):
                    res[i+1][j]="V"
                if j>0:
                    res[i][j-1]="V"
    return res