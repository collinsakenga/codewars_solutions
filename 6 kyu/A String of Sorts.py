def sort_string(s, ordering):
    temp=list(s)
    dict={}
    for i in set(s):
        dict[i]=s.count(i)
    res=""
    for i in ordering:
        if dict.get(i, 0):
            res+=dict.get(i, 0)*i           
            for _ in range(dict.get(i, 0)):
                temp.remove(i)
            dict[i]=0
    return res+"".join(temp)