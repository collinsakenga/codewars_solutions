def colorful(number):
    temp=str(number)
    res=[]
    check=set()
    for i in range(len(temp)):
        for j in range(0, len(temp)-i):
            res.append(multiply(temp[j:j+i+1]))
            check.add(res[-1])
            if len(res)!=len(check):
                return False
    return True
def multiply(s):
    total=1
    for i in s:
        total*=int(i)
    return total 