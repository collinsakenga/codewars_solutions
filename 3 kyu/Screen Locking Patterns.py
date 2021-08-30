dict={'A': ['B', 'CB', 'D', 'E', 'F', 'GD', 'H', 'IE'], 
      'B': ['A', 'C', 'D', 'E', 'F', 'G', 'HE', 'I'], 
      'C': ['AB', 'GE', 'D', 'E', 'F', 'B', 'H', 'IF'], 
      'D': ['A', 'B', 'C', 'E', 'FE', 'G', 'H', 'I'], 
      'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'], 
      'F': ['A', 'B', 'C', 'DE', 'E', 'G', 'H', 'I'], 
      'G': ['AD', 'B', 'CE', 'D', 'E', 'F', 'H', 'IH'], 
      'H': ['A', 'BE', 'C', 'D', 'E', 'F', 'G', 'I'], 
      'I': ['AE', 'B', 'F', 'D', 'E', 'CF', 'GH', 'H']}
def count_patterns_from(firstPoint, length):
    if length<=1 or length>9:
        return 1 if length==1 else 0
    return helper(firstPoint, length, {firstPoint}, {"":0}, 1, [firstPoint])
def helper(cur, target, went, res, n, order):
    if n>=target:
        if n==target==len(order):
            res[""]+=1
        return
    length=len(went)
    for i in dict[cur]:
        comp=went|{i[0]} if len(i)==1 else went|{i[0], i[1]}
        diff=len(comp)-length
        if (diff==1 and i[0] not in went) or diff==2:
            helper(i[0], target, comp, res, n+diff, order+[i[0]])
    return res[""]