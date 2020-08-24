def solve(time):
    m = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
         19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two', 23: 'twenty three',
         24: 'twenty four', 25: 'twenty five', 26: 'twenty six',
         27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine', 30: 'half'}
    h = {0: 'twelve', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
         6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'midnight'}
    res = time.split(":")
    if not int(res[1]):
        return h[12] if int(res[0]) == 0 else h[int(res[0]) % 12]+" o'clock"
    hour = int(res[0])
    flag = False
    min = "minutes" if (int(res[1]) > 1 and 60-int(res[1]) > 1) else "minute"
    if int(res[1]) > 30:
        hour += 1
        flag = True
    if hour == 0 or hour == 24:
        if int(res[1]) % 15 != 0:
            return f"{m[60-int(res[1])]} {min} to {h[12]}" if flag else f"{m[int(res[1])]} {min} past {h[12]}"
        return f"{m[60-int(res[1])]} to {h[12]}" if flag else f"{m[int(res[1])]} past {h[12]}"
    if int(res[1]) % 15 != 0:
        return f"{m[60-int(res[1])]} {min} to {h[hour%12]}" if flag else f"{m[int(res[1])]} {min} past {h[hour%12]}"
    return f"{m[60-int(res[1])]} to {h[hour%12]}" if flag else f"{m[int(res[1])]} past {h[hour%12]}"
