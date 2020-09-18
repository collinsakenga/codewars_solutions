def dup(arr):
    res = []
    for word in arr:
        index = 0
        rec = 0
        temp = ""
        while index < len(word):
            if word[index] == word[rec]:
                index += 1
            else:
                temp += word[rec]
                rec = index
        res.append(temp+word[-1])
    return res
