res="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
class SpreadSheetHelper(object):

    @classmethod
    def convert_to_display(cls, internal):
        x=""
        total=[0]
        count=0
        num=internal[0]
        while total[-1]<num+1:
            count+=1
            total.append(total[-1]+26**count)
        for i in range(count, 0, -1):
            temp=(26*(num-total[-2]))//(total[-1]-total[-2])
            x+=res[temp%26]
            num-=((total[-1]-total[-2])*temp)//26
            total.pop()
        return x+str(internal[1]+1)      
    @classmethod
    def convert_to_internal(cls, display):
        index=next(i for i,j in enumerate(display) if not j.isalpha())
        x, y=display[:index], int(display[index:])
        return (sum((res.index(j)+1)*(26**(len(x)-1-i)) for i,j in enumerate(x))-1, y-1)