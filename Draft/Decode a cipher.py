table={i:j for i,j in enumerate("abcdefghijklmnopqrstuvwxyz"+"abcdefghijklmnopqrstuvwxyz".upper())}
def decode(cipher, b, c):
    cipher.insert(0, 0)
    res=[]
    for i in range(1, len(cipher)):
        res.append(table[cipher[i]-cipher[i-1]-b-c])
    return "".join(res)