def alphabetic_pairs(s, n):
    first, second=s.upper()[:len(s)//2], s.upper()[len(s)//2:]
    if len(first)==len(second)==1:
        return [second+first]
    return [i+j for i,j in zip(first, second[n%len(second):]+second[:n%len(second)])]