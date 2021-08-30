def money_value(s):
    try:
        return eval(s.replace("$", "").lstrip("0"))
    except:
        return 0