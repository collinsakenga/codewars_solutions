def siegfried(week, txt):
    return week1(txt) if week==1 else week2(txt) if week==2 else week3(txt) if week==3 else week4(txt) if week==4 else week5(txt)
def week1(s):
    temp=list(s)
    for i in range(0, len(temp)-1):
        check="".join(temp[i:i+2]).lower()
        if check=="ci" or check=="ce":
            temp[i]="S" if temp[i].isupper() else "s"
    for i,j in enumerate(temp):
        if j.lower()!="c":
            continue
        if i==len(temp)-1:
            temp[i]="K" if temp[i].isupper() else "k"
        elif temp[i+1].lower()!="h":
            temp[i]="K" if temp[i].isupper() else "k"
    return "".join(temp)
def week2(s):
    temp=list(week1(s))
    res=""
    index=0
    while index<len(temp):
        if index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="ph":
            res+="F" if temp[index].isupper() else "f"
            index+=1
        else:
            res+=temp[index] 
        index+=1
    return res
def week3(s):
    temp=week2(s).split(" ")
    for i,j in enumerate(temp):
        res=""
        count=0
        extra=""
        for k,l in enumerate(j):
            if not (l.isalpha() or l=="-" or l=="'"):
                extra=j[k:]
                break
            if l.isalpha():
                count+=1
            if l=='-':
                if count>3 and res[-1]=="e":
                    res=res[:-1]
                count=0
            elif res and res[-1].lower()==l.lower():
                continue
            res+=l
        if count>3 and res[-1]=="e":
            res=res[:-1]
        temp[i]=res+extra
    return " ".join(temp)
def week4(s):
    temp=list(week3(s))
    res=""
    index=0
    while index<len(temp):
        if index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="th":
            res+="Z" if temp[index].isupper() else "z"
            index+=1
        elif index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="wr":
            res+="R" if temp[index].isupper() else "r"
            index+=1
        elif index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="wh":
            res+="V" if temp[index].isupper() else "v"
            index+=1
        elif temp[index].lower()=="w":
            res+="V" if temp[index].isupper() else "v"
        else:
            res+=temp[index]
        index+=1
    return res
def week5(s):
    temp=list(week4(s))
    res=""
    index=0
    while index<len(temp):
        if index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="ou":
            res+="U" if temp[index].isupper() else "u"
            index+=1
        elif index<len(temp)-1 and "".join(temp[index:index+2]).lower()=="an":
            res+="Un" if temp[index].isupper() else "un"
            index+=1
        else:
            res+=temp[index]
        index+=1
    final=res.split(" ")
    for i,j in enumerate(final):
        res=""
        count=0
        extra=""
        for k,l in enumerate(j):
            if not (l.isalpha() or l=="-" or l=="'"):
                extra=j[k:]
                break
            res+=l
        if res[:2].lower()=="sm":
            res="Schm"+res[2:] if res[0].isupper() else "schm"+res[2:]
        if res[-3:].lower()=="ing":
            res=res[:-3]+"ink"
        final[i]=res+extra
    return " ".join(final)