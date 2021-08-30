def pennies(value, coins):
    remain=[i for i in coins if value>=i]
    res=helper(value, remain, [], {})
    if not res:
        return []
    return [list(i) for i in res.keys()]
def helper(cur, coins, arr, res):
    if cur==0:
        res[tuple(arr)]=1
        return 
    elif not coins:
        return 
    count=cur//coins[0]
    for i in range(count, 0, -1):
        helper(cur-i*coins[0], coins[1:], arr+[coins[0]]*i, res)
    helper(cur, coins[1:], arr, res)
    return res