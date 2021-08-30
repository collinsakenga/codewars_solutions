def speedify(st): 
    res=[" "]*(len(st)+26)
    for i,j in enumerate(st):
        res[i+(ord(j)-ord("A"))]=j
    return "".join(res).rstrip(" ")