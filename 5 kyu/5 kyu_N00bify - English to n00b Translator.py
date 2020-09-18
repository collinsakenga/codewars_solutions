dict = {"be": "b", "before": "b4", "are": "r", "you": "u", "please": "plz", "people": "ppl",
        "really": "rly", "have": "haz", "know": "no", "fore": "4", "for": "4", "to": "2", "too": "2"}


def n00bify(text):
    text = text.replace("'", "").replace(",", "").replace(".", "")
    res = text.split()
    for i, j in enumerate(res):
        for k in range(len(j)-1):
            if j[k:k+2].lower() in dict:
                res[i] = j[:k]+dict[j[k:k+2].lower()]+j[k+2:] if j[k].islower() else j[:k] + \
                    dict[j[k:k+2].lower()].capitalize()+j[k+2:]
            elif j[k:k+2].lower() == "oo":
                res[i] = res[i].replace(j[k:k+2], "00")
        for k in range(len(j)-2):
            if j[k:k+3].lower() in dict:
                res[i] = j[:k]+dict[j[k:k+3].lower()]+j[k+3:] if j[k].islower() else j[:k] + \
                    dict[j[k:k+3].lower()].capitalize()+j[k+3:]
        for k in range(len(j)-3):
            if j[k:k+4].lower() in dict:
                res[i] = j[:k]+dict[j[k:k+4].lower()]+j[k+4:] if j[k].islower() else j[:k] + \
                    dict[j[k:k+4].lower()].capitalize()+j[k+4:]
        for k in range(len(j)-5):
            if j[k:k+6].lower() in dict:
                res[i] = j[:k]+dict[j[k:k+6].lower()]+j[k+6:] if j[k].islower() else j[:k] + \
                    dict[j[k:k+6].lower()].capitalize()+j[k+6:]
        res[i] = res[i].replace("S", "Z").replace("s", "z")
    if res[0][0].lower() == "h":
        for i, j in enumerate(res):
            res[i] = j.upper()
    elif res[0][0].lower() == "w":
        res.insert(0, "LOL")
    temp = " ".join(res)
    if (len(temp)-temp.count("?")-temp.count("!")) >= 32:
        res.insert(1, "OMG") if res[0] == "LOL" else res.insert(0, "OMG")
    for i, j in enumerate(res):
        if (i+1) % 2 == 0:
            res[i] = j.upper()
        if "?" in j:
            res[i] = res[i].replace("?", "?"*len(res))
        if "!" in j:
            exclamation = ""
            for k in range(len(res)):
                exclamation += "!" if k % 2 == 0 else "1"
            res[i] = res[i].replace("!", exclamation)
    return " ".join(res)
