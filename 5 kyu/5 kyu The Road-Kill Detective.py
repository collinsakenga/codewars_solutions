from collections import Counter
def road_kill(photo):
    res=""
    temp=""
    total=""
    for i in photo:
        if i=="=":
            continue
        elif not i.isalpha():
            return "??"
        total+=i
        if i!=temp:
            res+=i
        temp=i
    filter="".join(i for i in res if not i.islower())
    total=Counter(total)
    if filter:
        return "??"
    for i in ANIMALS:
        if i==res or i==res[::-1]:
            return i
        string=""
        for char in i:
            if not string:
                string+=char
            else:
                if string[-1]!=char:
                    string+=char
        if not (Counter(i)-total) and (string==res or string==res[::-1]):
            return i
    return "??"