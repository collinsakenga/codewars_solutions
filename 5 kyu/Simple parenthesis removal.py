def solve(s):
    res=[]
    cur=""
    math=""
    for i in s:
        if i=="(":
            if not res or res[-1]=="":
                res.append(cur)
            elif cur=="":
                res.append(res[-1])
            elif res[-1]==cur:
                res.append("+")
            elif res[-1]!=cur:
                res.append("-")
            cur=""
        elif i==")":
            res.pop()
        elif i in "+-":
            cur=i
        else:
            if res:
                if (cur=="" and res[-1]==""):
                    math+="+"+i
                elif cur=="":
                    math+="+"+i if res[-1]=="+" else "-"+i
                elif res[-1]=="":
                    math+="+"+i if cur[-1]=="+" else "-"+i
                elif cur==res[-1]:
                    math+="+"+i
                elif cur!=res[-1]:
                    math+="-"+i
            else:
                math+="+"+i  if cur!="-" else "-"+i
    return math.lstrip("+")