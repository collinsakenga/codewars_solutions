dict={'b': 1, 'c': 2, 'd': 3, 'f': 1, 'g': 2, 'j': 2, 'k': 2, 'l': 4, 'm': 5, 'n': 5, 'p': 1, 'q': 2, 'r': 6, 's': 2, 't': 3, 'v': 1, 'x': 2, 'z': 2}
def soundex(name):
    res=[]
    for i in name.split():
        temp="".join(k for j,k in enumerate(i.lower()) if not (k in "hw" and j!=0))
        temp2="".join(str(dict.get(j, j)) for j in temp)
        temp3=""
        for k in temp2:
            if temp3 and temp3[-1]==k:
                continue
            temp3+=k
        temp4="".join(k for j,k in enumerate(temp3) if not (k in "aeiouy" and j!=0))
        temp4=temp[0].upper()+temp4[1:] if temp[0] in dict else temp4.upper()
        res.append(temp4.ljust(4, "0")[:4])
    return " ".join(res)