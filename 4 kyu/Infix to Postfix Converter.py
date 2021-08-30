pref={'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1}
def to_postfix (infix):
    stack=[]
    res=[]
    for i in infix:
        if i.isdigit():
            res.append(i)
        elif i=="(":
            stack.append(i)
        elif i==")":
            while stack:
                op=stack.pop()
                if op=="(":
                    break
                res.append(op)
        else:
            if i=="^" and (stack and stack[-1]=="^"):
                stack.append(i)
                continue
            while stack and pref[stack[-1]]>=pref[i]:
                res.append(stack.pop())
            stack.append(i)
    return "".join(res+stack[::-1])