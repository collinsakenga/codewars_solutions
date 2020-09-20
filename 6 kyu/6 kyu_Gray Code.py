def bin2gray(bits):
    res = [0] if bits[0] == 0 else [1]
    for i in range(1, len(bits)):
        if bits[i] == 1 and bits[i-1] == 1:
            res.append(0)
        elif bits[i] == 0 and bits[i-1] == 0:
            res.append(0)
        else:
            res.append(1)
    return res


def gray2bin(bits):
    res = [0] if bits[0] == 0 else [1]
    for i in range(1, len(bits)):
        if bits[i] == 1 and bits[i-1] == 1:
            res.append(0)
            bits[i] = 0
        elif bits[i] == 0 and bits[i-1] == 0:
            res.append(0)
            bits[i] = 0
        else:
            res.append(1)
            bits[i] = 1
    return res
