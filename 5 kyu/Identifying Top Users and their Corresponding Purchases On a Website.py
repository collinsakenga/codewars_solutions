from copy import deepcopy
def id_best_users(*args):
    dict={}
    length=len(args)
    for i,j in enumerate(args):
        dict2={}
        for k in j:
            dict2[k]=dict2.get(k, 0)+1
            if not dict.get(k, None):
                dict[k]=[1,1]
            else:
                dict[k][0]+=1
                if dict2[k]==1:
                    dict[k][1]+=1
    final={k:v for k,v in sorted({k:v for k,v in dict.items() if v[1]==length}.items(), key=lambda x: -x[1][0])}
    res=[]
    for i,j in final.items():
        if not res:
            res.append([j[0], [i]])
        elif res[-1][0]==j[0]:
            res[-1][1].append(i)
        else:
            res.append([j[0], [i]])
    for i,j in enumerate(res):
        res[i][1]=sorted(j[1])
    return res