from operator import add, sub, mul, truediv
def calculate(expression):
    test=expression
    if any(i not in ".0123456789+-*$" for i in expression):
        return '400: Bad request'
    for notation, cal in zip("$*", (truediv, mul)):
        arr=expression.split(notation)
        while len(arr)>1:
            i1=next((i for i in range(len(arr[0])-1, -1, -1) if arr[0][i] in "+-*$"), -1)
            i2=next((i for i in range(len(arr[1])) if arr[1][i] in "+-*$"), len(arr[1]))
            left, right=float(arr[0][i1+1:]), float(arr[1][:i2])
            mid=str(cal(left, right))
            if "e" in mid:
                mid="%.16f" % float(mid)
            ans=arr[0][:i1+1]+mid+arr[1][i2:]
            del arr[:2]
            arr.insert(0, ans)
        expression=arr[0].replace("e", "")
    index=next((i for i,j in enumerate(expression) if j in "+-*/"), len(expression))
    res=[float(expression[:index])]
    temp=""
    pre=None
    for i in expression[index:]+"+":
        if i in "+-":
            if pre:
                if pre=="+":
                    res.append(res.pop()+float(temp))
                elif pre=="-":
                    res.append(res.pop()-float(temp))
            pre=i
            temp=""
        else:
            temp+=i
    return res.pop()