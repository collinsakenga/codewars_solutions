def clean_string(s):
    result = []
    for i in s:
        if i == "#":
            if result:
                result.pop(-1)
        else:
            result.append(i)
    return "".join(result)
