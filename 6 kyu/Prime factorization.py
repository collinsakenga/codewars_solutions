class PrimeFactorizer:
    def __init__(self, n):
        self.factor={}
        temp=[]
        factor=2
        while factor*factor<=n:
            if n%factor==0:
                temp.append(factor)
                n//=factor
                factor=2
            else:
                factor+=1
        temp.append(n)
        for i in set(temp):
            self.factor[i]=temp.count(i)