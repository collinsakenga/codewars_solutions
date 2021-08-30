def subtract_sum(num):
    while True:
        for value in str(num):
            num-=int(value)
        if num<100:
            break
    if num%9==0:
        return "apple"