def combos(n):
    return [list(i) for i in helper(n, [], set())]
def helper(n, arr, memo):
    memo.add(tuple(sorted(arr+[n])))
    for i in range(1, n):
        helper(n-i, arr+[i], memo)
    return memo