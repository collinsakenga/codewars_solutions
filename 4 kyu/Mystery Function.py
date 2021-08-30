def mystery(n):
    num=bin(n)[2:]
    res=num[0]
    for i in range(len(num)-1):
        res+="1" if (int(num[i])+int(num[i+1]))==1 else "0"
    return int(res, 2)
def mystery_inv(n):
    num=bin(n)[2:]
    res=num[0]
    for i in range(len(num)-1):
        res+="1" if (int(res[-1])+int(num[i+1]))==1 else "0"
    return int(res, 2)
def name_of_mystery():
    return 'Gray code'