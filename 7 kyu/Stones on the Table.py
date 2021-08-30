def solution(stones):
    total=0
    check=set()
    rec=0
    for i,j in enumerate(stones):
        check.add(j)
        if len(check)==2:
            total+=i-rec-1
            rec=i
            check={j}
    return total+len(stones)-rec-1