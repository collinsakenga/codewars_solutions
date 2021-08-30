def autocorrect(input):
    res=[]
    for i in input.split():
        index=next((j for j,k in enumerate(i) if not k.isalpha()), len(i))
        check=i[:index].lower()
        if check=="u" or (check.startswith("you") and check[3:]=="u"*(len(check)-3)):
            res.append("your sister"+i[index:])
        else:
            res.append(i)
    return " ".join(res)
            