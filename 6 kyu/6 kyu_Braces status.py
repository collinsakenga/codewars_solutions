def braces_status(string):
    if "[)" in string or "[}" in string or "(}" in string or "(]" in string or "{)" in string or "{]" in string:
        return False
    one=two=three=0
    for i in string: 
        if i=="(":
            one+=1 
        elif i==")": 
            one-=1 
        elif i=="[":
            two+=1  
        elif i=="]":
            two-=1 
        elif i=="{":
            three+=1
        elif i=="}":
            three-=1
        if one<0 or two<0 or three<0:
            return False
    return True if(one==0 and two==0 and three==0) else False