def fat_fingers(string):
    res=""
    flag=False
    for i in string:
        if i in "aA":
            flag=not flag
            continue
        if not i.isalpha():
            res+=i
        else:
            res+=i if not flag else i.lower() if i.isupper() else i.upper()
    return res