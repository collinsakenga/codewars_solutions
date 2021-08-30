def high(x):
    x=x.split()
    total=0
    comp=0
    index=0
    compindex=0
    for word in x:
        for char in word:
            total+=ord(char)-ord('a')+1
        if total>comp:
            comp=total
            compindex=index
        index+=1
        total=0
    return x[compindex]