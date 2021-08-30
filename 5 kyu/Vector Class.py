class Vector:
    def __init__(self, vect):
        self.vect=list(vect)
    def __str__(self):
        return "("+",".join([str(i) for i in self.vect])+")"
    def add(self, others):
        self.error_check(others)
        temp=list(self.vect)
        for i in range(len(temp)):
            temp[i]=self.vect[i]+others.vect[i]
        return Vector(temp)
    def subtract(self, others):
        self.error_check(others)
        temp=list(self.vect)
        for i in range(len(temp)):
            temp[i]=self.vect[i]-others.vect[i]
        return Vector(temp)
    def norm(self):
        sum=0
        for i in self.vect:
            sum+=i**2
        return sum**0.5
    def dot(self, others):
        self.error_check(others)
        sum=0
        for i,j in enumerate(self.vect):
            sum+=j*others.vect[i]
        return sum
    def __eq__ (self, others):
        if len(self.vect)!=len(others.vect):
            return False
        for i in range(len(self.vect)):
            if self.vect[i]!=others.vect[i]:
                return False
        return True
    def equals(self, others):
        return self.vect==others.vect
    def error_check(self, others):
        if len(self.vect)!=len(others.vect):
            raise Exception("Wrong")