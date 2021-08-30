from math import ceil
def union_jack(n):
    if not (isinstance(n, int) or isinstance(n, float)):
        return False
    length=max(7, ceil(n))
    res=[]
    split="-"*((length-3)//2)
    line=list(split.join(["X", "X", "X"])) if length%2==1 else list(split.join(["X", "X"])*2)
    for i in range((length-1)//2):
        res.append("".join(line))
        line[i], line[i+1]=line[i+1], line[i]
        line[-i-1], line[-i-2]=line[-i-2], line[-i-1]
    return "\n".join(res+["X"*length]*(2-length%2)+res[::-1])
    