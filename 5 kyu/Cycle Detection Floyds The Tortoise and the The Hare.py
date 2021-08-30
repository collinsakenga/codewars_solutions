def floyd(f, x0):
    return helper(f, x0, {}, 0)
def helper(f, n, memo, index):
    if n in memo:
        return [memo[n], index-memo[n]]
    memo[n]=index
    return helper(f, f(n), memo, index+1)