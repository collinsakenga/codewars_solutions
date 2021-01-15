def valid(a):
    dict={}
    length_word=len(a[0][0])
    length_arr=len(a[0])
    for i in a:
        if len(i)!=length_arr:
            return False
        for j in i:
            if len(j)!=length_word:
                return False
            for k,l in enumerate(j):
                for m in j[:k]+j[k+1:]:
                    if not dict.get(l, None):
                        dict[l]={m:1}
                    elif not dict[l].get(m, None):
                        dict[l][m]=1
                    else:
                        return False
    return len({sum(j for j in i.values()) for i in dict.values()})==1