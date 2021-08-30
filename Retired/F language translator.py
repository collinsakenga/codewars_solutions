def ftranslator(string):
    return "".join(i+f"f{i}" if i in "aeiou" else i for i in string.lower())