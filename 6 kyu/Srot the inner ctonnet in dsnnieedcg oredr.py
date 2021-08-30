def sort_the_inner_content(words):
    res=words.split()
    for i,j in enumerate(res):
        if len(j)<=3:
            continue
        res[i]=j[0]+"".join(sorted(j[1:-1], reverse=True))+j[-1]
    return " ".join(res)