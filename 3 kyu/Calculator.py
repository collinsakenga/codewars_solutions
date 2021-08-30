class Calculator(object):
    def evaluate(self, string):
        try:
            return float(string)
        except:
            pass
        string=string.replace(" ","")
        for cal in "/*-+":
            temp=string.split(cal)
            for i in range(0,len(temp)-1):
                print(temp)
                if not temp[i]:
                    continue
                digit1=int(self.extract_right(temp[i],cal)) if "." not in self.extract_right(temp[i],cal) else float(self.extract_right(temp[i],cal))
                digit2=int(self.extract_left(temp[i+1],cal)) if "." not in self.extract_left(temp[i+1],cal) else float(self.extract_left(temp[i+1],cal))
                num=self.operation(digit1, digit2, cal) 
                temp[i]=temp[i][0:len(temp[i])-len(str(digit1))]
                temp[i+1]=str(num)+temp[i+1][len(str(digit2)):]
            string="".join(temp)
        print(string)
        return float(string)
    def extract_right(self, string, cal):
        index=0
        for j,i in enumerate(string):
            if i in "+-*/" and (string[0]!="-" or (string.count("+")+string.count("/")+string.count("*")+string.count("-")>1)):
                index=j
        if index==0 and len(string)>1: return string
        return string[index+1:] if (len(string)>1) else string[index:]
    def extract_left(self, string, cal):
        index=len(string)
        flag=False
        for j,i in enumerate(string):
            if i in "+-*/":
                if not flag and (string[0]=="-"):
                    flag=True
                    continue
                else:
                    index=j
                    break
        return string[:index] if len(string)>1 else string[:index]
    def operation(self, num1, num2, determine):
        if determine=="+":
            return num1+num2
        elif determine=="-":
            return num1-num2
        elif determine=="*":
            return num1*num2
        elif determine=="/":
            return num1/num2