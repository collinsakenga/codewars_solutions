def parse(data):
    result = []
    temp = 0
    for i in data:
        if i == "i":
            temp += 1
        elif i == "d":
            temp -= 1
        elif i == "s":
            temp = temp**2
        elif i == "o":
            result.append(temp)
    return result
