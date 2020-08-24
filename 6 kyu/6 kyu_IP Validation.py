def is_valid_IP(strng):
    strng = strng.split(".")
    if len(strng) != 4:
        return False
    for i in strng:
        try:
            temp = int(i)
            if temp < 0:
                return False
            elif temp > 255:
                return False
            elif temp >= 0 and temp <= 9 and len(i) > 1:
                return False
            elif temp >= 10 and temp <= 99 and len(i) > 2:
                return False
        except:
            return False
    return True
