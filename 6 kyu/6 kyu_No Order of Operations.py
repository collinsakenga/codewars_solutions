def no_order(equation):
    temp = "".join(equation.split())
    while True:
        sign = ""
        first = ""
        for i, j in enumerate(temp):
            if j in "+-*/%^" and i != 0:
                index = i+1
                sign = j
                break
            first += j
        if not sign:
            break
        second = ""
        stop = len(temp)
        for i in range(index, len(temp)):
            if temp[i] in "+-*/%^":
                stop = i
                break
            second += temp[i]
        try:
            if sign == "+":
                result = int(first)+int(second)
            elif sign == "-":
                result = int(first)-int(second)
            elif sign == "*":
                result = int(first)*int(second)
            elif sign == "/":
                result = int(first)//int(second)
            elif sign == "%":
                result = int(first) % int(second)
            elif sign == "^":
                result = int(first)**int(second)
            temp = str(result)+temp[stop:]
        except:
            return None
    return int(temp)
