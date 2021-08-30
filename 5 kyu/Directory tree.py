from typing import List

def tree(root: str, files: List[str]):
    table={}
    for i in files:
        path=[root]+i.split("/")
        cur=table
        for file in path:
            if file not in cur:
                cur[file]={}
            cur=cur[file]
    res=iterate(table, [])
    return res or root
def iterate(table, cur):
    table={i:j for i,j in sorted(table.items(), key=lambda x: (0 if table[x[0]] else 1, x[0]))}
    last=len(table.keys())-1
    res=[]
    for index, i in enumerate(table.keys()):
        if not cur:
            res.append(i)
        elif index==last:
            res.append("   ".join(cur[:-1]+["└── "])+i)
        else:
            res.append("   ".join(cur[:-1]+["├── "])+i)
        if not cur or index!=last:
            if cur: cur[-1]="│"
            res+=iterate(table[i], cur+["│"])
        else:
            cur[-1]=" "
            res+=iterate(table[i], cur+[" "])
    return res