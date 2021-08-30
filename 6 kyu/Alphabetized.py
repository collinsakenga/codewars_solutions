def alphabetized(s):    
    filter_string=""
    for i in s:
        if i.isalpha():
            filter_string+=i
    if not filter_string:
        return ""
    temp=list(filter_string)
    solution="" 
    while temp:
        index=255
        for i in temp:
            index=min(ord(i.lower()), index)
        for i in temp:
            if ord(i.lower())==index:
                solution+=i
                temp.remove(i)
                break
    return solution