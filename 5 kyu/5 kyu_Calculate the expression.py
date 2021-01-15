def calculate(input):
    if not isinstance(input, str):
        return False
    res="".join(i for i in input if i!=" ")
    solution=temp=""
    for i in res:
        if i.isdigit():
            temp+=i
        elif i in "+-*/":
            if not temp:
                return False
            solution+=(temp.lstrip("0") or "0")+i
            temp=""
        else:
            return False
    if not temp:
        return False
    try:
        return eval(solution+(temp.lstrip("0") or "0"))
    except:
        return False