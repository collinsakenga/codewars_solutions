def encipher(s, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    rec = s
    temp = []
    s = s.lower()
    flag = True
    for i in key.lower():
        if i not in temp and i.isalpha():
            temp.append(i)
            alphabet.remove(i)
    if "i" in temp and "j" in temp:
        if temp.index("i") > temp.index("j"):
            temp.remove("i")
            flag = False
        elif temp.index("j") > temp.index("i"):
            temp.remove("j")
    elif "i" in temp:
        alphabet.remove("j")
    elif "j" in temp:
        alphabet.remove("i")
        flag = False
    else:
        alphabet.remove("j")
    s = s.replace("j", "i") if flag else s.replace("i", "j")
    temp2 = temp+alphabet
    s = "".join(s.split())
    while True:
        compare = len(s)
        for i in range(0, compare-1):
            if s[i+1] == s[i]:
                s = s[:i+1]+"x"+s[i+1:]
        if compare == len(s):
            break
    s += "x" if len(s) % 2 != 0 else ""
    result = [s[i:i+2] for i in range(0, len(s), 2)]
    final = ""
    for i in result:
        index1 = temp2.index(i[0])
        index2 = temp2.index(i[1])
        if index1//5 == index2//5:
            index3 = index1//5 * 5 + (index1+1) % 5
            index4 = index2//5 * 5 + (index2+1) % 5
        elif index1 % 5 == index2 % 5:
            index3 = (index1+5) % 25
            index4 = (index2+5) % 25
        else:
            index3 = index1+(index2 % 5-index1 % 5)
            index4 = index2+(index1 % 5-index2 % 5)
        final += temp2[index3]+temp2[index4]
    final = final.upper()
    count = 0
    for i in range(0, len(rec)):
        if rec[i].isalpha():
            rec = rec[:i]+final[count]+rec[i+1:]
            count += 1
    return rec+final[count:]