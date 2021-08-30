import string

def is_pangram(s):
    temp=list(set(s.lower()))
    temp.sort()
    temp="".join(temp)
    return True if "abcdefghijklmnopqrstuvwxyz" in temp else False