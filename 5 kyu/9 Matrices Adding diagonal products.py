from functools import reduce
mul=lambda arr: reduce(lambda x, y: x*y, arr)
def sum_prod_diags(matrix):
    return helper(matrix)
def helper(matrix):
    diagL, diagR={}, {}
    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            diagL[k+i]=diagL.get(k+i, [])+[l]
            diagR[k-i]=diagR.get(k-i, [])+[l]
    return sum(mul(v) for v in diagR.values())-sum(mul(v) for v in diagL.values())