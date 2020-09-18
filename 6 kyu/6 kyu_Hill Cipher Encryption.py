def encrypt(text, key):
    matrix = [[None]*2 for i in range(2)]
    for i, j in enumerate(key):
        matrix[i//2][i % 2] = ord(j)-ord("a")
    temp = "".join(i for i in text if i.isalpha())
    res = ""
    for i in range(0, len(temp), 2):
        first = ord(temp[i:i+1])-ord("a") if temp[i:i +
                                                  1].islower() else ord(temp[i:i+1])-ord("A")
        try:
            second = ord(temp[i+1:i+2])-ord("a") if temp[i +
                                                         1:i+2].islower() else ord(temp[i+1:i+2])-ord("A")
        except:
            second = 25
        res += chr(ord("A")+(matrix[0][0]*first+matrix[0][1]*second) %
                   26)+chr(ord("A")+(matrix[1][0]*first+matrix[1][1]*second) % 26)
    return res
