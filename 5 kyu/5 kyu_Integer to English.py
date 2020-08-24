units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
         "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
         "sixteen", "seventeen", "eighteen", "nineteen", "placeholder"]
ten = ["placeholder", "placeholder", "twenty", "thirty", "forty", "fifty",
       "sixty", "seventy", "eighty", "ninety"]
hundred = ["hundred"]
times = ["placeholder", "thousand", "million", "billion", "trillion",
         "quadrillion", "quintillion", "sextillion", "septillion"]


def intToEng(string):
    temp = int(string)
    res = []
    if temp < 20:
        return units[temp]
    if temp >= 100:
        res.append(units[temp//100])
        res.append("hundred")
        temp -= (temp//100)*100
    if temp >= 20:
        res.append(ten[temp//10])
        temp -= (temp//10)*10
    if temp > 0:
        res.append(units[temp])
    return " ".join(res)


def int_to_english(n):
    result = str(n)
    final = []
    if len(result) % 3 != 0:
        result = "0"*(3-len(result) % 3)+result
    index = len(result)//3-1
    record = index
    temp = result
    slice = 0
    while index >= 0:
        num = temp[slice:slice+3]
        string = intToEng(num)
        if int(num) != 0:
            final.append(string)
            if index > 0:
                final.append(times[index])
        index -= 1
        slice += 3
    return " ".join(final)
