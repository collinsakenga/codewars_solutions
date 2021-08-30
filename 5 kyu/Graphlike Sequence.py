def solution(degrees):
    res=sorted(degrees)
    while res:
        num=res.pop(0)
        index=len(res)-1
        while index>=0 and num:
            res[index]-=1
            num-=1
            index-=1
        res.sort()
        if num:
            return False
    return True