def square_digits(num):
    s=str(num)
    res=""
    for i in s:
        res+=str(int(i)**2)
    return int(res)