def phone(strng, num):
    check=strng.count(num)
    if check>1:
        return f"Error => Too many people: {num}"
    elif check==0:
        return f"Error => Not found: {num}"
    for i in strng.split("\n"):
        if num not in i:
            continue
        name=[]
        address=[]
        for j in i.split():
            if num in j:
                continue
            if "<" in j or ">" in j:
                temp=j
                temp=temp[1:] if "<" in temp else temp
                temp=temp[:-1] if ">" in temp else temp
                name.append(temp)
            else:
                address.append(j.replace("_", " ").replace(",", "").replace("/", "").replace(";", "").strip(" "))
        name=" ".join(name)
        address=" ".join(address)
        break
    return f"Phone => {num}, Name => {name}, Address => {address}"