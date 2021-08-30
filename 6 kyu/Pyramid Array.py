def pyramid(n):
    result=[]
    temp=[]
    for i in range(n):
        for j in range(-1,i):
            temp.extend([1])
        result.append(temp)
        temp=[]
    return result
      