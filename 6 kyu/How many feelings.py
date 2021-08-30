from collections import Counter
def count_feelings(s, arr):
    res=Counter(s)
    length=len([i for i in arr if not any(j for j,k in Counter(i).items() if k>res.get(j, 0))])
    return f"{length} feelings." if length!=1 else f"{length} feeling."