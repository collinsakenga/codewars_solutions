class helper():
    def __init__(self):
        self.matrix=[[0, 1, 0], [0, 0, 1], [1, 1, 0]]
    def multiply(self, other):
        a=self.matrix[0][0]*other[0][0]+self.matrix[0][1]*other[1][0]+self.matrix[0][2]*other[2][0]
        b=self.matrix[0][0]*other[0][1]+self.matrix[0][1]*other[1][1]+self.matrix[0][2]*other[2][1]
        c=self.matrix[0][0]*other[0][2]+self.matrix[0][1]*other[1][2]+self.matrix[0][2]*other[2][2]
        d=self.matrix[1][0]*other[0][0]+self.matrix[1][1]*other[1][0]+self.matrix[1][2]*other[2][0]
        e=self.matrix[1][0]*other[0][1]+self.matrix[1][1]*other[1][1]+self.matrix[1][2]*other[2][1]
        f=self.matrix[1][0]*other[0][2]+self.matrix[1][1]*other[1][2]+self.matrix[1][2]*other[2][2]
        g=self.matrix[2][0]*other[0][0]+self.matrix[2][1]*other[1][0]+self.matrix[2][2]*other[2][0]
        h=self.matrix[2][0]*other[0][1]+self.matrix[2][1]*other[1][1]+self.matrix[2][2]*other[2][1]
        i=self.matrix[2][0]*other[0][2]+self.matrix[2][1]*other[1][2]+self.matrix[2][2]*other[2][2]
        self.matrix[0][0]=a
        self.matrix[0][1]=b
        self.matrix[0][2]=c
        self.matrix[1][0]=d
        self.matrix[1][1]=e
        self.matrix[1][2]=f
        self.matrix[2][0]=g
        self.matrix[2][1]=h
        self.matrix[2][2]=i
def padovan(n):
    if n<=2:
        return 1
    res=helper()
    mul=[]
    while n>1:
        mul.append(divmod(n, 2)[1])
        n//=2
    for i in mul[::-1]:
        res.multiply(res.matrix)
        if i==1:
            res.multiply([[0, 1, 0], [0, 0, 1], [1, 1, 0]])
    return sum(res.matrix[0])