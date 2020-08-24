def encode(n, strng):
    strng = strng.replace("\n", "一")
    key = list("".join(strng.split()))
    result = strng
    for i in range(n):
        temp = key.copy()
        for i in range(len(key)):
            key[i] = temp[(i-n) % len(key)]
        count = 0
        for i in range(len(result)):
            if result[i] != " ":
                result = result[:i]+key[count % len(key)]+result[i+1:]
                count += 1
        rotate = result.split()
        for i in range(len(rotate)):
            if n % len(rotate[i]) == 0:
                continue
            word = rotate[i]
            word_key = list(word)
            for j in range(len(word_key)):
                word_key[j] = word[(j-n % len(word_key)) % len(word_key)]
            rotate[i] = "".join(word_key)
        key = list("".join(rotate))
    for i in range(len(result)):
        if result[i] != " ":
            result = result[:i]+key[count % len(key)]+result[i+1:]
            count += 1
    result = result.replace("一", "\n")
    return str(n)+" "+result


def decode(strng):
    n = ""
    for i in strng:
        try:
            j = int(i)
            n += i
        except:
            break
    strng = strng[len(n)+1:]
    n = int(n)
    strng = strng.replace("\n", "一")
    key = list("".join(strng.split()))
    result = strng
    for i in range(n):
        rotate = result.split()
        for i in range(len(rotate)):
            if n % len(rotate[i]) == 0:
                continue
            word = rotate[i]
            word_key = list(word)
            for j in range(len(word_key)):
                word_key[j] = word[(j+n % len(word_key)) % len(word_key)]
            rotate[i] = "".join(word_key)
        key = list("".join(rotate))
        count = 0
        temp = key.copy()
        for i in range(len(key)):
            key[i] = temp[(i+n) % len(key)]
        for i in range(len(result)):
            if result[i] != " ":
                result = result[:i]+key[count % len(key)]+result[i+1:]
                count += 1
    result = result.replace("一", "\n")
    return result
