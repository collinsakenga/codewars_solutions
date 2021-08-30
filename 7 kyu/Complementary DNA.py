def DNA_strand(s):
    c=""
    for i in range(len(s)):
        if s[i]=="A":
            c+="T"
        elif s[i]=="T":
            c+="A"
        elif s[i]=="G":
            c+="C"
        elif s[i]=="C":
            c+="G"
    return c