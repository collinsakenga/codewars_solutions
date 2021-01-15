def is_keith_number(n):
    if n<14:
        return False
    res=[int(i) for i in str(n)]
    count=1
    while sum(res)<n:
        count+=1
        res.append(sum(res))
        res.pop(0)
    return count if sum(res)==n else False