def find_secret_message(paragraph):
    dict={}
    paragraph="".join(i.lower() if i.isalpha() else i if (i==" " or i=="-") else "" for i in paragraph )
    res=[]
    for i in paragraph.split():
        if dict.get(i, None) and i not in res:
            res.append(i)
        dict[i.lower()]=1
    return " ".join(res)