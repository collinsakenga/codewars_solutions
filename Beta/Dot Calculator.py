def calculator(txt):
    res=txt.split()
    for i,j in enumerate(res):
        if "." in j:
            res[i]=str(len(j))
    return "."*eval("".join(res))