def disemvowel(string):
    return "".join(i for i in string if not (i.lower() in "aeiou"))