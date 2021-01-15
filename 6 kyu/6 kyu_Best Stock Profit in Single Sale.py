def max_profit(prices):
    dict={}
    check=max(prices[1:])
    for i in range(len(prices)-1):
        if prices[i]==check:
            check=max(prices[i+1:])
        dict[i]=check
    comp=-1
    for i,j in enumerate(prices[:-1]):
        comp=max(comp, dict[i]-j)
    return comp 