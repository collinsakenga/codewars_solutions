def knapsack(capacity, items):
    dict={i:j for i,j in enumerate(items)}
    temp=sorted(dict.items(), key=lambda x: (-(x[1][1]/x[1][0])))
    res=[0]*len(items)
    num=capacity
    for i,j in temp:
        if num//j[0]:
            res[i]=num//j[0]
            num-=num//j[0]*j[0]
    return res