def scramble_words(words):
    res=[]
    for i in words.split():
        if len(i)<=2:
            res.append(i)
            continue
        start=next((j for j,k in enumerate(i) if k.isalpha()), 0)
        end=next((j for j,k in enumerate(i[::-1]) if k.isalpha()), 0)
        index=next((j for j in i if not j.isalpha()), None)
        if not index:
            res.append(i[0]+"".join(sorted(i[1:-1]))+i[-1])
        else:
            temp=i if (not start and not end) else i[start:] if not end else i[:-end] if not start else i[start:-end]
            index=[j for j,k in enumerate(temp) if not k.isalpha()]
            if not index:
                string=i[:start]+temp[0]+"".join(sorted(temp[1:-1]))+temp[-1]
                if end:
                    string+=i[-end:]
                res.append(string)
            else:
                letters=[temp[j] for j in index]
                sorted_string=[temp[0]]+sorted(j for j in temp[1:-1] if j.isalpha())+[temp[-1]]
                for j,k in zip(letters, index):
                    sorted_string.insert(k, j)
                string=i[:start]+"".join(sorted_string)
                if end:
                    string+=i[-end:]
                res.append(string)
    return " ".join(res)