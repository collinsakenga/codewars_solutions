def syllable_separator(string):
    res, arr, add=[], [], False
    for char in string:
        arr.append(char)
        if char in "aeiou":
            add=True
        elif add:
            res.append("".join(arr))
            add, arr=False, []
    if arr: res.append("".join(arr))
    return "-".join(res)