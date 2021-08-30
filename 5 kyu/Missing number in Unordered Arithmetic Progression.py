def find(seq):
    seq.sort()
    dict={}
    flag=False
    for i in range(len(seq)-1):
        dict[seq[i+1]-seq[i]]=dict.get(seq[i+1]-seq[i], 0)+1
        if flag and dict[seq[i+1]-seq[i]]==1:
            return (seq[i+1]+seq[i])//2
        if not flag and dict[seq[i+1]-seq[i]]>=2:
            flag=True 
    return (seq[0]+seq[1])//2