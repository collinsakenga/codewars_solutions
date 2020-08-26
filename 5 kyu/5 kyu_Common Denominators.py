from fractions import gcd


def convertFracts(lst):
    temp = [lst[i][j] for i in range(len(lst)) for j in range(len(lst[i]))]
    temp = [temp[i:i+2] for i in range(0, len(temp), 2)]
    for i in range(0, len(temp)-1):
        temp[i+1][1] = temp[i][1]*temp[i+1][1]//gcd(temp[i][1], temp[i+1][1])
    for i in range(0, len(lst)):
        lst[i][0] = temp[-1][1]//lst[i][1]*lst[i][0]
        lst[i][1] = temp[-1][1]
    return lst
