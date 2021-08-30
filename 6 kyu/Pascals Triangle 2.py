def pascal(p):
    result=[[1],[1,1]]
    if p==1:
        return [[1]]
    elif p==2:
        return result
    temp=[1]
    for i in range(2,p):
        for j in range(0,len(result[i-1])-1):
            temp.append(result[i-1][j]+result[i-1][j+1])
        temp.append(1)
        result.append(temp)
        temp=[1]
    return result