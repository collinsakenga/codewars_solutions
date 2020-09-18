def solve_runes(runes):
    temp = runes
    digit = 0
    while digit < 10:
        if str(digit) in temp:
            digit += 1
            continue
        length = temp[temp.index('=')+1:]
        rec = temp.replace("?", str(digit))
        answer = rec[rec.index("=")+1:]
        rec = rec[:rec.index("=")]
        try:
            if eval(rec) == int(answer) and len(str(int(answer))) == len(length):
                return digit
        except:
            pass
        digit += 1
    return -1
