def unique_digit_products(a):
    res=set()
    for i in a:
        num=1
        temp=str(i)
        for j in temp:
            num*=int(j)
        res.add(num)
    return len(res)