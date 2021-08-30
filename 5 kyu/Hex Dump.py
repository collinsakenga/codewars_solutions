def hexdump(data):
    res=[]
    for index, i in enumerate(range(0, len(data), 16)):
        prefix=hex(index)[2:].rjust(7, "0")+"0"
        arr=[hex(char)[2:].rjust(2, "0") for char in data[i:i+16]]
        arr+=["  "]*(16-len(arr))
        transform="".join(chr(char) if 32<=char<=126 else "." for char in data[i:i+16])
        code=" ".join(arr)
        res.append(f"{prefix}: {code}  {transform}")
    return "\n".join(res)
def dehex(text):
    res=[]
    for i in text.split("\n"):
        letters=i.split(": ")[1].split("  ")[0]
        res.extend(chr(int(i, 16)) for i in letters.split())
    return bytes("".join(res), encoding="raw_unicode_escape")