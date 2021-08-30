def pig_latin(s):
    if not s:
        return None
    res=""
    for i in s:
        if not i.isalpha():
            return None
        res+=i.lower()
    if res[0] in "aeiou":
        return res+"way"
    consonant=""
    for i in res:
        if i in "aeiou":
            break
        consonant+=i
    return res[len(consonant):]+consonant+"ay"