def encode(string):
    res=""
    for i in string:
        res+="{0:08b}".format(ord(i))
    return res.replace("0","000").replace("1", "111")
def decode(bits):
    temp=""
    for i in range(0,len(bits), 3):
        temp+="1" if bits[i:i+3].count("1")>=2 else "0"
    res=""
    for i in range (0, len(temp), 8):
        res+=chr(int(temp[i:i+8], 2))
    return res