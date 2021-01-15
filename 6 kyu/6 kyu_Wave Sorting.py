from copy import deepcopy
def wave_sort(arr):
    res=sorted(arr)
    solution=[]
    while res:
        if res: 
            solution.append(res[-1])        
        if res and len(res)>1: 
            solution.append(res[0])
        if res:
            res.pop()
        if res:
            res.pop(0)
    for i in range(len(solution)):
        arr[i]=solution[i]