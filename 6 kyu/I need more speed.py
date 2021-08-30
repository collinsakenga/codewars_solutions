def reverse(seq):
    for i in range(0,len(seq)//2):
        temp=seq[i]
        seq[i]=seq[len(seq)-1-i]
        seq[len(seq)-1-i]=temp