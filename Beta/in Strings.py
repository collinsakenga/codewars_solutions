def encode_string(string):
    res=string.split()
    for i,j in enumerate(res):
        res[i]=j[::-1]
    return ">><<".join(res)+str(max(len(res)-1, 0))