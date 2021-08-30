def toUnderScore(name):
    if not name:
        return ""
    start="_" if name[0]=="_" else ""
    end="_" if name[-1]=="_" else ""
    name="".join(i for i in name if i!="_")
    res=""
    for i in name:
        if res and (i.isupper() or not (i.isalpha())):
            if not res[-1].isdigit():
                res+="_"
            elif i.isalpha():
                res+="_"
        res+=i
    return start+res+end