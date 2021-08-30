def dec(string,number):
    res=""
    for i in string:
        res+=chr((ord(i)-number)%126) if chr((ord(i)-number)%126)!="\x00" else "~"
    return res