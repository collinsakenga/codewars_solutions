def zeros(n):
    check = 5
    digits = 0
    while n//check >= 1:
        digits += n//check
        check *= 5
    return digits
