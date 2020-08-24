def prime_string(s):
    append_string = ""
    for char in s:
        append_string += char
        if append_string == s:
            break
        if s.count(append_string)*len(append_string) == len(s):
            return False
    return True
