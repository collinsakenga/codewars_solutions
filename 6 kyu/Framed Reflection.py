def mirror(text):
    temp=text.split()
    length=0
    for i in temp:
        length=max(len(i), length)
    solution=""
    for i in temp:
        solution+="* "+i[::-1]+" "*(1+length-len(i))+"*"+"\n"
    return "*"*(length+4)+"\n"+solution+"*"*(length+4)