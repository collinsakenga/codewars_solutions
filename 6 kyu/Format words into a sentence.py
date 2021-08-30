def format_words(words):
    if not words:
        return ""
    while "" in words:
        words.remove("")
    if not words:
        return ""
    elif len(words)==1:
        return words[0]
    return ", ".join(words[:-1])+" and "+words[-1]