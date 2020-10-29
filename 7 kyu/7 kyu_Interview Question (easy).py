def get_strings(city):
    dict={}
    for i in city.lower():
        if not i.isalpha():
            continue
        dict[i]=dict.get(i, "")+"*"
    return ",".join(f"{i}:{j}" for i,j in dict.items())