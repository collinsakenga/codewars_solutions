colours=['red', 'yellow', 'blue']
def same_col_seq(val, k, col):
    if col=="yellow":
        return []
    res=[]
    num=increment=1
    while len(res)<k:
        if num>val and col==colours[(num-1)%3]:
            res.append(num)
        num, increment=num+increment+1, increment+1
    return res