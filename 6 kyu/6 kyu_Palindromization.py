def palindromization(elements, n):
    if not elements or n<=1:
        return "Error!"
    temp=elements*(n//(2*len(elements)))+elements[:(n%((2*len(elements))))//2]
    temp2=elements*(n//(2*len(elements)))+elements[:(n%((2*len(elements))))//2+1]
    if n%2==0:
        return temp+temp[::-1]
    return temp2+temp[::-1]