def royalfam(n):
    total, temp=0, ""
    for i in n+"'":
        if i.isdigit():
            temp+=i
        else:
            total+=int(temp or "0")**2*2
            temp=""
    return total