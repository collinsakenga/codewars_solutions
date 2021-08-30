def chocolate_maker(small, big, x):
    return any(i*5+j==x for i in range(big+1) for j in range(small+1))