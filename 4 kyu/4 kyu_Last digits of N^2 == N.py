def memo():
    res=[1, 5, 6]
    count=10
    count2=100
    last_five, last_six=5, 6
    while len(res)<5000:
        temp1=None
        for i in range(count, count2, count):
            num=i+last_five
            if (num**2)%count2==num:
                temp1=num
                break
        temp2=None
        for i in range(count, count2, count): 
            num=i+last_six
            if (num**2)%count2==num:
                temp2=num
                break
        if temp1 and temp2:
            if temp1>temp2:
                res.append(temp2)
                res.append(temp1)
            else:
                res.append(temp1)
                res.append(temp2)
            last_five, last_six=temp1, temp2
        elif temp1:
            res.append(temp1)
            last_five=temp1
        elif temp2:
            res.append(temp2)
            last_six=temp2
        count*=10
        count2*=10
    return res 
count=memo()
def green(n):
    return count[n-1]