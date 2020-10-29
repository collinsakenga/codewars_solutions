def atomic_number(electrons):
    res=[]
    power=1
    while electrons:
        num=min(2*(power**2), electrons)
        res.append(num)
        electrons-=num
        power+=1
    return res