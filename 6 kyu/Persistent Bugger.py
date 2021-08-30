def persistence(num):
    count=0
    while True:
        num2=1
        if num>=0 and num <=9:
            break
        for i in range (len(str(num))):
            num2*=int(str(num)[i])
        num=num2
        count+=1
    return count