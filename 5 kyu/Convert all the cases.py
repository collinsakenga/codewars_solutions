check=["snake", "camel", "kebab"]
def change_case(identifier, targetCase):
    if targetCase not in check:
        return None
    if not valid(identifier):
        return None
    if not identifier:
        return ""
    if targetCase=="snake":
        return snake(identifier)
    elif targetCase=="camel":
        return camel(identifier)
    elif targetCase=="kebab":
        return kebab(identifier)
    return ""
def snake(s):
    for i in s:
        if i.isupper():
            s=s.replace(i,"_"+i.lower())
    return s.replace("-", "_")
def camel(s):
    index=0
    temp=list(s)
    for i in range(len(temp)):
        if temp[i-index] in "-_":
            temp.pop(i-index)
            temp[i-index]=temp[i-index].upper()
            index+=1
    return "".join(temp)
def kebab(s):
    if "_" in s:
        return s.replace("_", "-")
    index=0
    temp=list(s)
    for i in range(len(temp)):
        if temp[i+index].isupper():
            temp.insert(i+index, "-")
            temp[i+index+1]=temp[i+index+1].lower()
            index+=1
    return "".join(temp)
def valid(s):
    if s.count("-")>=1 and s.count("_")>=1:
        return False
    if s.lower()!=s and (s.count("-")>=1 or s.count("_")>=1):
        return False
    return True