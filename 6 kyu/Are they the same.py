from math import sqrt
def comp(array1, array2):
    if array1==None or array2==None:
        return False
    if len(array1)==0 and len(array2)==0:
        return True
    if len(array1)==0 or len(array2)==0:
        return False
    array1.sort()
    array2.sort()
    count=0
    for num in array1:
        if num**2 not in array2:
            return False
        array2.remove(num**2)
    return True