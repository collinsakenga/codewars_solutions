dict={i:j for i,j in enumerate("zero one two three four five six seven eight nine".split())}
def numbers_of_letters(n):
    res=["".join(dict[int(i)] for i in str(n))]
    while True:
        num=len(res[-1])
        res.append("".join(dict[int(i)] for i in str(num)))
        if res[-2]==res[-1]:
            break
    return res[:-1]