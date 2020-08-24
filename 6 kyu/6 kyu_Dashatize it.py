def dashatize(num):
    try:
        num = abs(num)
    except:
        return "None"
    if len(str(num)) == 1:
        return str(num)
    result = ""
    check = 0
    check2 = len(str(num))-1
    count = 0
    for i in str(num):
        if int(i) % 2 == 1:
            if count == check:
                result += f"{i}-"
            elif count == check2:
                result += f"-{i}"
            else:
                result += f"-{i}-"
        else:
            result += i
        count += 1
    return result.replace("--", "-")
