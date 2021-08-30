def encode(string):
    s=string
    comp=len(string)
    num=perfect(comp)
    power=num**2
    for i in range(power-comp):
        s+=" "
    temp = [[0]*num for _ in range(num)]
    res = 1
    left = 0
    right = len(temp)-1
    up = 0
    down = len(temp)-1
    index = 0
    while True:
        if temp[up][left+index] != 0:
            up += 1
            right -= 1
            left += 1
            down -= 1
            index = 0
        temp[up][left+index] = res
        res += 1
        if res > power:
            break
        temp[up+index][right] = res
        res += 1
        if res > power:
            break
        temp[down][right-index] = res
        res += 1
        if res > power:
            break
        temp[down-index][left] = res
        res += 1
        if res > power:
            break
        index += 1
    for i in range(0,num):
        for j in range(0,num):
            temp[i][j]=s[temp[i][j]-1]
    final=""
    for i in temp:
        final+="".join(i)
    return final
def decode(string):
    res=""
    temp1=1
    temp2=int(len(string)**0.5)
    temp3=len(string)
    temp4=temp3-temp2+1
    comp1=temp1
    comp2=temp2
    comp3=temp3
    comp4=temp4
    increment=temp2
    while True:
        if temp1==comp2:
            temp1=comp1+increment+1
            temp2=comp2+increment-1
            temp3=comp3-increment-1
            temp4=comp4-increment+1
            comp1=temp1
            comp2=temp2
            comp3=temp3
            comp4=temp4
        res+=string[temp1-1]
        temp1+=1        
        if len(res)==len(string):
            break
        res+=string[temp2-1]
        temp2+=increment
        if len(res)==len(string):
            break
        res+=string[temp3-1]
        temp3-=1
        if len(res)==len(string):
            break
        res+=string[temp4-1]
        temp4-=increment
        if len(res)==len(string):
            break
    return res.rstrip()
def perfect(num):
    test=1
    while test**2<num:
        test+=1
    return test