def pattern(rows, columns, s):
    boundary = "---".join(["+"]*(columns+1))
    res = [boundary]
    s = s+(rows*columns-len(s))*" "
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(s[i*columns+j])
        res.append("| "+" | ".join(temp)+" |")
        res.append(boundary)
        temp = []
    return "\n".join(res)
