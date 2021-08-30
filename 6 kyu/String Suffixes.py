def string_suffix(str_):
    total=0
    for i in range(1,len(str_)):
        for j,k in enumerate(str_[i:]):
            if k!=str_[j]:
                break
            total+=1
    return total+len(str_)