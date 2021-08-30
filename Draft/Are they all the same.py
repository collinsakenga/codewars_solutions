def same_by(l, arr):
    return "Same!" if len(set(l(i) for i in arr))==1 else "Different..."