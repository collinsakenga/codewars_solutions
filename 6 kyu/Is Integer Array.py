def is_int_array(arr):
    if arr==[]:
        return True
    if not arr:
        return False
    for i in arr:
        try:
            temp=int(i)
            if temp-i!=0.0:
                return False
        except:
            return False
    return True