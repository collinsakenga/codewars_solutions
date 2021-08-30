def string_color(name):
    if len(name)<2:
        return None
    return first(name)+second(name)+third(name)
def first(s):
    return hex(sum(ord(i) for i in s)%256)[2:].rjust(2, "0").upper()
def second(s):
    total=1
    for i in s:
        total*=ord(i)
    return hex(total%256)[2:].rjust(2, "0").upper()
def third(s):
    return hex(abs(ord(s[0])-sum(ord(i) for i in s[1:]))%256)[2:].rjust(2, "0").upper()