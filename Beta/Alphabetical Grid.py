from string import ascii_lowercase
def grid(N):
    if N<0:
        return None
    word=list(ascii_lowercase[i%26] for i in range(N))
    res=[]
    for _ in range(N):
        res.append(" ".join(word))
        word.pop(0)
        word.append(ascii_lowercase[(N+_)%26])
    return "\n".join(res)