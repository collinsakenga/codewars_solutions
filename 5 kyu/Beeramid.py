def beeramid(bonus, price):
    if bonus//price<=0:
        return 0
    result=int(bonus/price)
    index,check,total=1,1,0
    while total<result:
        check+=1+2*index
        total+=check
        index+=1
    return index-1