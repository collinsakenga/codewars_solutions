def matches(snippet):
    temp=""
    left={}
    for i in snippet:
        temp+=i
        if ">" in temp:
            add="".join(i for i in temp if i.isalpha())
            if "/" in temp:
                if not (add in left):
                    return False
                left[add]-=1
            else:
                left[add]=left.get(add, 0)+1
            temp=""
    return not any(i for i in left.values() if i!=0)