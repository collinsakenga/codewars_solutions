def parity_bit(binary):
    res=[]
    for i in binary.split():
        res.append("error") if i[:-1].count("1")%2!=int(i[-1]) else res.append(i[:-1])
    return " ".join(res)
