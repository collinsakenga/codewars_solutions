def stock_list(listOfArt, listOfCat):
    dict = {}
    for char in listOfCat:
        dict[char] = 0
    for i in listOfArt:
        if i[0][0] in dict:
            dict[i[0][0]] += int(i.split()[1])
    return format_string(dict)


def format_string(dict):
    res = []
    count = 0
    for i, j in dict.items():
        count = max(count, j)
        res.append(f"({i} : {j})")
    return " - ".join(res) if count else ""
