def monopoly(amount):
    res, cur={}, amount
    for i in (500, 100, 50, 20, 10, 5, 1):
        res[i], cur=cur//i, cur-cur//i*i
    return {i:j for i,j in res.items() if j}