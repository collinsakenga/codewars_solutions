def autocomplete(input_, dictionary):
    input_="".join(i for i in input_ if i.isalpha())
    res=[]
    index=0
    while len(res)<5 and index<len(dictionary):
        if dictionary[index].lower()[:len(input_)]==input_:
            res.append(dictionary[index])
        index+=1
    return res