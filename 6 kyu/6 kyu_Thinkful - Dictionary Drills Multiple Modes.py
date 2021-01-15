from collections import Counter
def modes(data):
    low, high=len(data), 0
    res=Counter(data)
    for i in res.values():
        high=max(high, i)
        low=min(low, i)
    if high==low:
        return []
    return sorted(i for i,j in res.items() if j==high)