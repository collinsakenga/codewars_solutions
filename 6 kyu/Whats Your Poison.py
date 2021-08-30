def find(r):
    res=["0"]*10
    for i in r:
        res[i]="1"
    return int("".join(res)[::-1], 2)