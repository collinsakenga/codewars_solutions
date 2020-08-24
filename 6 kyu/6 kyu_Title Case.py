def title_case(title, minor_words=''):
    if not title:
        return ""
    res = title.split(" ")
    for i in range(1, len(res)):
        if res[i].lower() in minor_words.lower().split(" "):
            res[i] = res[i].lower()
        else:
            res[i] = res[i].capitalize()
    return res[0].capitalize()+" "+" ".join(res[1:]) if len(res) > 1 else res[0].capitalize()
