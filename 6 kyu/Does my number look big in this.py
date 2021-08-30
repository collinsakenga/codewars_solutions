def narcissistic( num ):
    count=0
    temp=num
    comp=0
    while True:
        num=int(num/10)
        count+=1
        if num==0:
            break
    for i in range(len(str(temp))):
        comp+=int(str(temp)[i])**count
    if comp==temp:
        return True
    else:
        return False