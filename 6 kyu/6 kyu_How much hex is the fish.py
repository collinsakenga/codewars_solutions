dict={j:10+i for i,j in enumerate("abcdef")}
def fisHex(name):
    value="".join(i for i in name.lower() if i in "abcdef")
    if not value:
        return 0
    res=dict[value[0]]
    for i in value[1:]:
        res=res^dict[i]
    return res