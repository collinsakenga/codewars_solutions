def bin_to_hex(binary_string):
    res=binary_string.lstrip("0") or "0"
    decimal=sum(2**(len(res)-1-i) for i,j in enumerate(res) if j=="1")
    power=0
    while decimal>=16**(power+1):
        power+=1
    check={i:j for i,j in enumerate("0123456789abcdef")}
    res=""
    while power>=0:
        value=decimal//(16**power)
        res+=check[value]
        decimal-=value*(16**power)
        power-=1
    return res
def hex_to_bin(hex_string):
    res=hex_string.lstrip("0").lower() or "0"
    check={j:i for i,j in enumerate("0123456789abcdef")}
    decimal=sum(16**(len(res)-1-i)*check[j] for i,j in enumerate(res))
    power=0
    while decimal>=2**(power+1):
        power+=1
    res=""
    while power>=0:
        value=decimal//(2**power)
        res+="1" if value else "0"
        decimal-=value*(2**power)
        power-=1
    return res