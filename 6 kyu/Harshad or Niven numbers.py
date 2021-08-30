class Harshad:
    @staticmethod
    def is_valid(number):
        return True if number%Harshad.digit_sum(number)==0 else False   
    @staticmethod
    def get_next(number):
        next=number+1
        while True:
            if Harshad.is_valid(next):
                return next
            next+=1    
    @staticmethod
    def get_series(count, start=0):
        res=[]
        for i in range(count):
            res.append(Harshad.get_next(start))
            start=Harshad.get_next(start)
        return res
    @staticmethod
    def digit_sum(n):
        total=0
        for i in str(n):
            total+=int(i)
        return total