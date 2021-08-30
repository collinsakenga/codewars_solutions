from math import factorial
def sum_arrangements(num):
    total=0
    temp=str(num)
    times=factorial(len(temp)-1)
    for i in "123456789":
        total+=temp.count(i)*(int(i))*times*10**(len(temp)-1)
    multiply="1"*len(temp)
    return total*int(multiply)//(10**(len(temp)-1))