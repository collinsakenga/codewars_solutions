def solve_postfix(expr):
    try:
        return int(expr)
    except:
        if not expr:
            return 0
        res=expr.split()
        while "+" in res or "-" in res or "*" in res or "/" in res or "^" in res:
            for i,j in enumerate(res):
                if j in "+-*/^":
                    index=i
                    break
            first=res[index-2]
            second=res[index-1]
            solution=operations(first+" "+res[index]+" "+second)
            res=res[:(index-2)]+[str(solution)]+res[index+1:]
        return int(res[0])
def operations(s):
    res=s.split()
    if res[1]=="+":
        return int(int(res[0])+int(res[2]))
    elif res[1]=="-":
        return int(int(res[0])-int(res[2]))
    elif res[1]=="*":
        return int(int(res[0])*int(res[2]))
    elif res[1]=="/":
        return int(int(res[0])//int(res[2]))
    elif res[1]=="^":
        return (int(res[0])**int(res[2]))