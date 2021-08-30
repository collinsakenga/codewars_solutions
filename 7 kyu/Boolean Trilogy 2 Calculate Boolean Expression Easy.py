def calculate(expr, values):  
    for i in expr.split(" | "):
        flag=next((0 for j in i.split(" & ") if values[j]==0), 1)
        if flag:
            return 1
    return 0