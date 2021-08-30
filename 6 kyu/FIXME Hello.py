class Dinglemouse(object):
    
    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None
        self.index=0
    def setAge(self, age):
        if not self.age:
            self.age = [age, self.index] 
        else: 
            self.age[0]=age;
        self.index+=1
        return self
        
    def setSex(self, sex):
        if not self.sex:
            self.sex = [sex, self.index]
        else: 
            self.sex[0]=sex;
        self.index+=1
        return self
        
    def setName(self, name):
        if not self.name:
            self.name = [name, self.index]
        else: 
            self.name[0]=name;
        self.index+=1
        return self
        
    def hello(self):
        res=[item for item, extra in sorted([i for i in [self.name, self.age, self.sex] if i], key=lambda x:(x[1]))]
        str=["Hello."]
        for i in res:
            if self.name and i==self.name[0]:
                str.append(f"My name is {self.name[0]}.")
            elif self.sex and i==self.sex[0]:
                str.append("I am male.") if i =="M" else str.append("I am female.")
            elif self.age and i==self.age[0]:
                str.append(f"I am {self.age[0]}.")
        return " ".join(str)