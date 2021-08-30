def get_consective_items(items, key): 
    item, k=str(items), str(key)
    comp=temp=0
    for i in item:
        if i==k:
            temp+=1
        else:
            comp=max(temp, comp)
            temp=0
    return max(comp, temp)