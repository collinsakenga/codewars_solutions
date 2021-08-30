def decompose(n):
    return helper(n, n**2)
def helper(n, sum, arr=[]):
    if sum==0:
        return arr[::-1]
    for i in range(n-1, -1, -1):
        if i**2<=sum:
            return helper(i, sum-i**2, arr+[i]) or helper(i, sum, arr) 