def find_reverse_number(n):
    if n<=10:
        return n-1
    res=str(n)
    if res[0]!="1":
        s=chr(ord(res[0])-1)+res[1:]
        return int(s+s[-2::-1])
    index=2 if res[:2]=="10" else 1
    s=str(int(res[:index])-1).lstrip("0")+res[index:]
    return int(s+s[::-1]) if index==1 else int(s+s[-2::-1])