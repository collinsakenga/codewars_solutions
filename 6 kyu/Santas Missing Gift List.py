def gifts(number):
    res=bin(number)[2:]
    return sorted([GIFTS[2**(len(res)-1-i)] for i,j in enumerate(res) if j=="1"])