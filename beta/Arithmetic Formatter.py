def arithmetic_formatter(problems):
    if len(problems)>5:
        return "Error: Too many problems."
    elif any(j in "*/" for i in problems for j in i):
        return "Error: Operator must be '+' or '-'."
    elif any(j not in "0123456789+- " for i in problems for j in i):
        return "Error: Numbers must only contain digits."
    elif any(len(j)>4 for i in problems for j in i.split()):
        return "Error: Numbers cannot be more than four digits."
    res=[[], [], [], []]
    for i in problems:
        first, op, second=i.split()
        length=max(len(first), len(second))+2
        res[0].append(first.rjust(length, " "))
        res[1].append(op+second.rjust(length-1, " "))
        res[2].append("-"*length)
        res[3].append(str(eval(first+op+second)).rjust(length, " "))
    return "\n".join("    ".join(i) for i in res)