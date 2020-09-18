def bowling_pins(arr):
    return "\n".join([first(arr), second(arr), third(arr), fourth(arr)])


def first(arr):
    if 7 in arr and 8 in arr and 9 in arr and 10 in arr:
        res = " "*7
    elif 7 in arr and 8 in arr and 9 in arr:
        res = "      I"
    elif 7 in arr and 8 in arr and 10 in arr:
        res = "    I  "
    elif 7 in arr and 9 in arr and 10 in arr:
        res = "  I    "
    elif 10 in arr and 8 in arr and 9 in arr:
        res = "I      "
    elif 7 in arr and 8 in arr:
        res = "    I I"
    elif 7 in arr and 9 in arr:
        res = "  I   I"
    elif 7 in arr and 10 in arr:
        res = "  I I  "
    elif 8 in arr and 9 in arr:
        res = "I     I"
    elif 8 in arr and 10 in arr:
        res = "I   I  "
    elif 9 in arr and 10 in arr:
        res = "I I    "
    elif 7 in arr:
        res = "  I I I"
    elif 8 in arr:
        res = "I   I I"
    elif 9 in arr:
        res = "I I   I"
    elif 10 in arr:
        res = "I I I  "
    else:
        res = "I I I I"
    return res


def second(arr):
    if 4 in arr and 5 in arr and 6 in arr:
        res = " "*7
    elif 4 in arr and 5 in arr:
        res = "     I "
    elif 5 in arr and 6 in arr:
        res = " I     "
    elif 4 in arr and 6 in arr:
        res = "   I   "
    elif 4 in arr:
        res = "   I I "
    elif 5 in arr:
        res = " I   I "
    elif 6 in arr:
        res = " I I   "
    else:
        res = " I I I "
    return res


def third(arr):
    if 2 in arr and 3 in arr:
        res = " "*7
    elif 2 in arr:
        res = "    I  "
    elif 3 in arr:
        res = "  I    "
    else:
        res = "  I I  "
    return res


def fourth(arr):
    res = " "*7 if 1 in arr else "   I   "
    return res
