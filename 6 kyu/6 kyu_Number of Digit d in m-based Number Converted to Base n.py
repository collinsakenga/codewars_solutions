sequence = "0123456789abcdefghijklmnopqrstuvwxyz"


def count_digit(number, digit, base=10, from_base=10):
    if base == 10 and from_base == 10:
        return number.count(digit)
    test = convert_dec(number, from_base)
    res = convert_target(test, base)
    return res.count(digit)


def convert_dec(s, base):
    num = 0
    for i, j in enumerate(s):
        num += sequence.index(j)*base**(len(s)-1-i)
    return num


def convert_target(num, base):
    power = 0
    while base**(power+1) < num:
        power += 1
    string = ""
    while power >= 0:
        temp = num//(base**power)
        string += sequence[temp]
        num -= num//(base**power)*base**power
        power -= 1
    return string
