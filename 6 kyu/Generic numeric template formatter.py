def numeric_formatter(template, replace="1234567890"):
    res=list(template)
    index=0
    for i,j in enumerate(res):
        if not (j.isdigit() or j in "+-*/" or j==" "):
            res[i]=replace[index%len(replace)]
            index+=1
    return "".join(res)
        