def monkey_talk(phrase):
    res=" ".join("eek" if j[0] in "aeiouAEIOU" else "ook" for j in phrase.split())
    return res[0].upper()+res[1:]+"."