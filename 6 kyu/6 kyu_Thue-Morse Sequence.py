def thue_morse(n):
    res = "0"
    while len(res) < n:
        temp = ""
        for i in res:
            temp += "0" if i == "1" else "1"
        res += temp
    return res[:n]
