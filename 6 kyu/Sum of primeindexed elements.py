from math import sqrt
def total(arr):
    sum=0
    for i in range(2,len(arr)):
        if isprime(i):
            sum+=arr[i]
    return sum
def isprime(num):
    for i in range(2,int(sqrt(num))+1):
        if num%i==0:
            return False
    return True