def calc(expr):
    try:
        return eval(expr)
    except:
        if not expr:
            return 0
        res=expr.split()
        while "+" in res or "-" in res or "*" in res or "/" in res:

            for i,j in enumerate(res):
                if j in "+-*/":
                    index=i
                    break
            first=res[index-2]
            second=res[index-1]
            solution=eval(first+res[index]+second)
            res=res[:(index-2)]+[str(solution)]+res[index+1:]
        return float(res[0])                   