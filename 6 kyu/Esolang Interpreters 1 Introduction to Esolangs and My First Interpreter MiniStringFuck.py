def my_first_interpreter(code):
    res=[]
    for i in "".join(i for i in code if i=="+" or i==".").split("."):
        res.append(len(i)%256) if not res else res.append((res[-1]+len(i))%256)
    return "".join(chr(i) for i in res)[:-1]