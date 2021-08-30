dict={j:i for i,j in enumerate("0123456789X")}
def valid_ISBN10(isbn): 
    if len(isbn)!=10 or (any(not i.isdigit() for i in isbn) and isbn[-1]!="X") or isbn.count("X")>1:
        return False  
    return sum(dict[j]*(i+1) for i,j in enumerate(isbn))%11==0