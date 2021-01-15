def mark_spot(n):
    if not isinstance(n, int) or n<=0 or n%2==0:
        return "?"
    res=[]
    line=list("X"+" "*(n*2-3)+"X")
    for i in range(n//2):
        res.append("".join(line).rstrip())
        line[i*2], line[(i+1)*2]=line[(i+1)*2], line[i*2]
        line[-(i*2)-1], line[-((i+1)*2)-1]=line[-((i+1)*2)-1], line[-(i*2)-1]
    return "\n".join(res+[" "*(n-1)+"X"]+res[::-1])+"\n"