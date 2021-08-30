from math import gcd
def lcm(*args):
    temp=list(args)
    if len(temp)==1: return temp[0]
    elif not temp: return 1
    for i in range(len(temp)-1):
        temp[i+1]=cal(temp[i], temp[i+1])
    return temp[-1]
def cal(num1, num2):
    return num1*num2//gcd(num1, num2)