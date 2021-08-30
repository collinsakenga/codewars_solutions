def group_check(s):
    if len(s)%2==1:
        return False
    comp=len(s)
    while True:
        if "()" in s:
            s=s.replace("()","")
        elif "[]" in s:
            s=s.replace("[]","")
        elif "{}" in s:
            s=s.replace("{}","")
        if len(s)==0:
            return True
        if comp==len(s):
            return False
        elif comp>len(s):
            comp=len(s)
        