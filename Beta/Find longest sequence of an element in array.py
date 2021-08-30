# return the length of the longest sequence of the value in the array
def longest_sequence(arr, elem):
    if elem not in arr:
        return 0 
    comp=0
    res=[i for i,j in enumerate(arr) if j!=elem]  
    if not res:
        return 0 
    res.append(len(arr)) 
    res.insert(0, -1)
    for i in range(1, len(res)):
        comp=max(comp, res[i]-res[i-1]-1)
    return comp