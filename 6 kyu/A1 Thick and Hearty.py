def a1_thick_and_hearty(a1, a2):
    set1, set2=set(a1), set(a2)
    common={i for i in set1 if i in set2}
    res=set()
    for i in common:
        if (i!=i-len(set1) and (i-len(set1)) in common) or (i!=i+len(set1) and (len(set1)+i) in common) or (i!=i-len(set2) and (i-len(set2)) in common) or (i!=i+len(set2) and (len(set2)+i) in common) or (i!=len(set1)-i and (len(set1)-i) in common) or (i!=len(set2)-i and (len(set2)-i) in common):
            res.add(i)
    return set(res)