def scanner(qrcode):
    res="".join(helper(i, qrcode) for i in range(4))
    return "".join(chr(int(res[i:i+8], 2)) for i in range(12, 12+int(res[4:12], 2)*8, 8))
def helper(index, qrcode):
    res=""
    for i in range([20, 9][index%2], [8, 21][index%2], [-1, 1][index%2]):
        for j in range(20-index*2, 20-(index+1)*2, -1):
            res+=str(qrcode[i][j]) if (i+j)%2 else "0" if qrcode[i][j]==1 else "1"
    return res