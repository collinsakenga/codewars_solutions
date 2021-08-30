data={j:i for i,j in enumerate("abcdefghijklmnopqrstuvwxyz")}
def keyword_cipher(msg, keyword):
    word=msg.lower()
    dict={i:"" for i in "abcdefghijklmnopqrstuvwxyz"}
    sub={i:"" for i in keyword}
    for i in sub.keys():
        del dict[i]
    res={i:j for i,j in enumerate({**sub, **dict})}
    s=""
    for i in word:
        s+=i if not i.isalpha() else res[data[i]]
    return s
        