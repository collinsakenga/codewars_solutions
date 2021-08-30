from collections import Counter
def added_char(s1, s2):  
    temp1, temp2=Counter(s1), Counter(s2)
    for i,j in temp2.items():
        try:
            if j-temp1[i]>0:
                return i
        except:
            return i