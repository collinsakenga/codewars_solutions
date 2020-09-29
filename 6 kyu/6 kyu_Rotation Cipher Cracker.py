def decode(msg, contents):
    res = []
    for i in range(26):
        temp = ""
        for char in msg:
            temp += chr(ord("a")+(ord(char)-ord("a")+i) %
                        26) if char.islower() else chr(ord("A")+(ord(char)-ord("A")+i) % 26)
        if contents in temp:
            res.append(temp)
    return res
