def ideal_trader(prices):
    arr=[]
    for i in prices:
        if not arr or arr[-1]!=i:
            arr.append(i)
    total=1
    start=arr[0]
    for i in arr[1:]:
        if i>start:
            total*=i/start
        else:
            total*=start/i
        start=i
    return total