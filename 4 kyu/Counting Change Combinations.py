def count_change(money, coins):
    remain=[i for i in coins if money>=i]
    if money==0 or remain==[]:
        return 1 if money==0 else 0
    res=helper(money, remain,{"count":0})
    return res["count"]
def helper(money, coins, memo):
    if money==0:    
        memo["count"]+=1 
        return
    elif len(coins)==0:
        return
    count=money//coins[0]
    for i in range(1, count+1):
        helper(money-i*coins[0], coins[1:],memo)
    helper(money, coins[1:], memo)
    return memo