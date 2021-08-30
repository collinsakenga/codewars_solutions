def number_increasing(n):
    num=n
    while True:
        if num<=1:
            return num==1
        if (num-1)%5==0:
            return True
        elif num%3==0:
            num//=3
        else:
            num-=5