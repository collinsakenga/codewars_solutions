def decompose(num):
    mul=2
    res=[[]]
    while True:
        power=0
        while mul**(power+1)<=num:
            power+=1
        if power<=1:
            break
        num-=mul**power
        mul+=1
        res[0].append(power)
    res.append(num)
    return res