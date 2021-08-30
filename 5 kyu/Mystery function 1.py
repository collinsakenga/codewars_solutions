def solved(s):
    if len(s)%2==0:
        return "".join(sorted(s))
    return "".join(sorted(j for i,j in enumerate(s) if i !=len(s)//2))
    