def accum(s):
    return "-".join(j.upper()+j.lower()*i for i,j in enumerate(s))