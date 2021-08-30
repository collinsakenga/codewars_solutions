from copy import deepcopy
def find_subarr_maxsum(arr):
    compare=[]
    total=0
    save={}
    for i in arr:
        compare.append(i)
        total+=i
        if total<0:
            compare=[]
            total=0
        else:
            if not save.get(total, None):
                save[total]=[deepcopy(compare)]
            else:
                save[total].append(deepcopy(compare))
    final=sorted(save.items(), key=lambda x: -x[0])
    if not final:
        return [[], 0]
    res=final[0]
    for i in res[1]:
        check=0
        for j,k in enumerate(i):
            check+=k
            if check==0:
                res[1].append(i[j+1:])
    if len(res[1])>1:
        return [res[1], res[0]]
    return [res[1][0], res[0]]