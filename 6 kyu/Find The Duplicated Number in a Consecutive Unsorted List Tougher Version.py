def find_dup(arr):
    dict={}
    for i in arr:
        if dict.get(i, None):
            return i
        dict[i]=1