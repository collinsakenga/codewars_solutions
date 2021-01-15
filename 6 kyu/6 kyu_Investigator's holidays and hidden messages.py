class Investigator:
    def __init__(self):
        self.list=[]
    def postcard(self, text):
        self.list.append(text)
    def hidden_message(self):
        return "".join(k for i in self.list for j,k in enumerate(i) if j>0 and ((k.isupper() and i[j-1].islower()) or (k==i[j-1]==" ")))