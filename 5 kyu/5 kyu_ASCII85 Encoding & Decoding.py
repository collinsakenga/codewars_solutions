def toAscii85(data):
    temp = ""
    for i in data:
        temp += "{:08b}".format(ord(i))
    rec = temp
    temp += "0"*(32-len(temp) % 32) if len(temp) % 32 else ""
    res = ""
    for i in range(0, len(temp), 32):
        for j in ascii85(temp[i:i+32], len(rec)//32):
            res += chr(j)
    return f"<~{res[:-(len(temp)-len(rec))//8]}~>" if len(temp)-len(rec) else f"<~{res}~>"


def fromAscii85(data):
    data = "".join(data[2:-2].replace("z", "!!!!!").split())
    temp = ""
    rec = len(data) % 5 if len(data) % 5 else 5
    data += chr(117)*(5-len(data) % 5) if len(data) % 5 else ""
    for i in range(0, len(data), 5):
        temp += convert(data[i:i+5])
    res = ""
    for i in range(0, len(temp)-(5-rec)*8, 8):
        res += chr(int(temp[i:i+8], 2))
    return res


def ascii85(num, check):
    if num.count("0") == 32 and check != 0:
        return [122]
    num = int(num, 2)
    arr = []
    index = 4
    while index >= 0:
        arr.append(num//85**index+33)
        num -= num//85**index*85**index
        index -= 1
    return arr


def convert(string):
    total = 0
    for i, j in enumerate(string):
        total += 85**(4-i)*(abs(ord(j)-33))
    return "{:032b}".format(total)
