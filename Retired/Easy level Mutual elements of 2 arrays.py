from collections import Counter
def mutual_elements(a,b):
    count1, count2=Counter(a), Counter(b)
    return sorted((i for i in (count1+count2).keys() if count1[i] and count2[i]))