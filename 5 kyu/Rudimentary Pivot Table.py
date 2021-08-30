def pivot(arr, index):
    dict={}
    flag={}
    for i,j in enumerate(arr[0]):
        if i==index:
            continue
        try:
            float(j)
            flag[i]=-1
        except:
            pass
    for i in arr:
        if not dict.get(i[index], None):
            dict[i[index]]=["-" if not flag.get(j, None) else float(k) for j,k in enumerate(i)]
        else:
            for k in flag.keys():
                dict[i[index]][k]+=float(i[k])
    temp=[v[:index]+[k]+v[index+1:] for k,v in dict.items()]
    return sorted(temp, key=lambda x: x[index])