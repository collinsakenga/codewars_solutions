def slogans(p,r):
    combo=set()
    for i in range(len(p)):
        for j in range(i, len(p)):
            combo.add(p[i:j+1])
    total=0
    index=0
    while True:
        flag=True
        for i in range(index, len(r)):
            if r[index:i+1] not in combo:
                index=i
                flag=False
                break
        total+=1
        if flag:
            break
    return total