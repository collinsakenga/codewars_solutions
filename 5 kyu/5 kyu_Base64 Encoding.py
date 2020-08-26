new = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def to_base_64(string):
    res = ""
    for i in string:
        res += binary(i)
    if len(res) % 6 != 0:
        res = res+"0"*(6-len(res) % 6)
    result = ""
    for i in range(0, len(res), 6):
        result += new[int(res[i:i+6], 2)]
    return result


def from_base_64(string):
    res = ""
    for i in string:
        res += binary2(i)
    result = ""
    for i in range(0, len(res), 8):
        result += chr(int(res[i:i+8], 2))
    return result.rstrip('\x00')


def binary(string):
    res = bin(ord(string))[2:]
    return "0"*(8-len(res))+res


def binary2(string):
    res = bin(new.index(string))[2:]
    return "0"*(6-len(res))+res
