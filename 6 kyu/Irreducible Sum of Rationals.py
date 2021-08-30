from copy import deepcopy
def sum_fracts(lst):
    if not lst:
        return None
    temp=deepcopy(lst)
    for i in range(len(temp)-1):
        temp[i+1][1]=lcm(temp[i][1], temp[i+1][1])
    total=0
    for i in range(len(temp)):
        total+=temp[-1][1]//lst[i][1]*lst[i][0]
    if total%temp[-1][1]==0: return total//temp[-1][1]
    divide=gcd(total, temp[-1][1])
    return [total//divide, temp[-1][1]//divide]
def gcd(a,b):
    if not b:
        return a
    return gcd(b, a%b)
def lcm(a,b):
    return a*b//gcd(a, b)
  