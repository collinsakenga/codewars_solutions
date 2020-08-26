def is_interesting(number, awesome_phrases):
    if number < 98:
        return 0
    elif check(number, awesome_phrases) and number >= 100:
        return 2
    for i in range(number+1, number+3):
        if i >= 100 and check(i, awesome_phrases):
            return 1
    return 0


def check(n, awesome_phrases):
    return equal(n) or all_zero(n) or increase(n) or decrease(n) or palindrome(n) or awesome(n, awesome_phrases)


def equal(n):
    return True if len(set(str(n))) == 1 else False


def all_zero(n):
    res = str(n)
    return True if int(res[1:]) == 0 else False


def increase(n):
    res = str(n)
    for i in range(len(res)-1):
        if not ((int(res[i+1])-int(res[i])) == 1 or ((int(res[i+1]) == 0 and int(res[i])) == 9)):
            return False
    return True


def decrease(n):
    res = str(n)
    for i in range(len(res)-1):
        if not (int(res[i])-int(res[i+1])) == 1:
            return False
    return True


def palindrome(n):
    return str(n) == str(n)[::-1]


def awesome(n, awesome_phrases):
    if not awesome_phrases:
        return False
    return n in awesome_phrases
