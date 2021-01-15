def f(s):
    for i in range(len(s)-1):
        if len(s)%(i+1)!=0:
            continue
        if s[:i+1]*(len(s)//(i+1))==s:
            return (s[:i+1], len(s)//(i+1))
    return (s, 1)