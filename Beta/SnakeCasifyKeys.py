def snake_casify(dictionary):
    for k in dictionary.keys():
        name="".join("_"+j.lower() if (i and j.isupper()) else j for i,j in enumerate(k))
        dictionary[name] = dictionary.pop(k)
    return dictionary