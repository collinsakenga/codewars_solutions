def cycle(n):
    if n%2==0 or n%5==0:
        return -1
    count=0
    value=1
    while True:
        value=value*10%n
        count+=1
        if value==1:
            return count