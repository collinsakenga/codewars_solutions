def fixed_xor(a, b):
    if not a or not b:
        return ""
    res=""
    for i,j in zip(a, b):
        temp1=bin(int(i, 16))[2:].rjust(4,"0")
        temp2=bin(int(j, 16))[2:].rjust(4,"0")
        for k,l in zip(temp1, temp2):
            res+="0" if k==l else "1"
    return "".join(hex(int(res[i:i+4], 2))[2:] for i in range(0, len(res), 4))