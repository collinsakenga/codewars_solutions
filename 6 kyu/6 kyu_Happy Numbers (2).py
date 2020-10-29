def happy_numbers(n):
    res=[]
    for i in range(1, n+1):
        dict={}
        temp=i
        while True:
            if temp==1:
                res.append(i)
                break
            elif dict.get(temp, None):
                break
            dict[temp]=1
            temp=square_sum(str(temp))
    return res
def square_sum(s):
    return sum(int(i)**2 for i in s)