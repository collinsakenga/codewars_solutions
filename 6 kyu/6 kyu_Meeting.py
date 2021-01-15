def meeting(s):
    dict={}
    for i in s.split(";"):
        temp=i.split(":")
        if not dict.get(temp[-1].upper(), None):
            dict[temp[-1].upper()]=[temp[0].upper()]
        else:
            dict[temp[-1].upper()].append(temp[0].upper())
    res=""
    for k, v in sorted(dict.items(), key=lambda x: x[0]):
        for name in sorted(v):
            res+=f"({k}, {name})"
    return res