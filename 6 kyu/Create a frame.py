def frame(text, char):
    length=0
    for i in text:
        length=max(len(i), length)
    res=[char*(length+4)]
    for i in text:
        res.append(char+" "+i+" "*(length-len(i))+" "+char)
    return "\n".join(res+[char*(length+4)])