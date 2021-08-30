def embrace():
    res, last=[9, 12], [9, 12]
    one, two="1001", "1100"
    for _ in range(7):
        temp=set()
        for i in last:
            num=bin(i)[2:]
            for j in range(len(num), 0, -2):
                temp.add(int(num[:j]+one+num[j:], 2))
                temp.add(int(num[:j]+two+num[j:], 2))
        last=sorted(temp)
        res.extend(last)
    for i in res:
        yield i