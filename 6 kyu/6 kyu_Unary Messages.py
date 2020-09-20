def send(s):
    res = []
    temp = "".join("{:07b}".format(ord(i)) for i in s)
    temp2 = ""
    for index in range(len(temp)):
        temp2 += temp[index]
        if len(set(temp2)) == 2:
            temp2 = temp2[:-1]
            res.append("0 "+"0"*len(temp2)
                       ) if temp2[0] == "1" else res.append("00 "+"0"*len(temp2))
            temp2 = temp[index]
    res.append("0 "+"0"*len(temp2)
               ) if temp2[0] == "1" else res.append("00 "+"0"*len(temp2))
    return " ".join(res)


def receive(s):
    bits = ""
    res = ""
    temp = s.split()
    for i in range(0, len(temp), 2):
        bits += "1"*len(temp[i+1]) if temp[i] == "0" else "0"*len(temp[i+1])
    for i in range(0, len(bits), 7):
        res += chr(int(bits[i:i+7], 2))
    return res
