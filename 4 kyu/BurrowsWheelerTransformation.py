def encode(s):
    matrix=[s]
    for i in range(1, len(s)):
        matrix.append(matrix[-1][-1]+matrix[-1][:-1])
    matrix.sort()
    string=""
    for i in range(len(s)):
        string+=matrix[i][-1]
    return (string, matrix.index(s))
def decode(s, n):
    if not s or n<0:
        return ""
    matrix=[[""]*len(s) for i in range(len(s))]
    first="".join(sorted(s))
    for i in range(len(matrix)):
        matrix[i][0]=first[i]
        matrix[i][-1]=s[i]
    for i in range(1, len(s)-1):
        temp=sorted(i[-1]+"".join(i[:-1]) for i in matrix)
        for j in range(len(s)):
            matrix[j][i]=temp[j][-1]
    return "".join(matrix[n])