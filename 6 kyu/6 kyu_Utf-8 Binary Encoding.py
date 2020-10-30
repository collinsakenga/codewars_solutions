def to_utf8_binary(string):
    res = ""
    for i in string:
        if ord(i) < 128:
            res += "{:08b}".format(ord(i))
        else:
            start = "110" if ord(i) < 2048 else "1110" if ord(
                i) < 65536 else "11110"
            temp = bin(ord(i))[2:].zfill(11+(len(start)-3)*5)
            index = 0
            for i in range(len(start)-1):
                if i == 0:
                    index += 8-len(start)
                    res += start+temp[:index]
                else:
                    res += "10"+temp[index:index+6]
                    index += 6
    return res


def from_utf8_binary(bitstring):
    res = ""
    while bitstring:
        if bitstring[:5] == "11110":
            res += chr(int(bitstring[5:8]+bitstring[10:16] +
                           bitstring[18:24]+bitstring[26:32], 2))
            bitstring = bitstring[32:]
        elif bitstring[:4] == "1110":
            res += chr(int(bitstring[4:8] +
                           bitstring[10:16]+bitstring[18:24], 2))
            bitstring = bitstring[24:]
        elif bitstring[:3] == "110":
            res += chr(int(bitstring[3:8]+bitstring[10:16], 2))
            bitstring = bitstring[16:]
        elif bitstring[0] == "0":
            res += chr(int(bitstring[:8], 2))
            bitstring = bitstring[8:]
    return res