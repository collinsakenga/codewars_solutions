def increment(number, iterations, spacer):
    res=[int(i) for i in list(str(number))]
    start=0
    for _ in range(iterations):
        start=(start+spacer)%len(res)
        res[start]+=1
        for i in range(start, 0, -1):
            if res[i]<10:
                continue
            res[i]-=10
            res[i-1]+=1
        if res[0]>=10:
            res[0]-=10
            res.insert(0, 1)
            start+=1
    return int("".join(str(i) for i in res))