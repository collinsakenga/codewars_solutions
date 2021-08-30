def cipher_text(plain_text):
    res="".join(i.lower() for i in plain_text if i.isalpha())
    print(res)
    if not res:
        return ""
    n=len(res)**0.5
    square=len(res) if n==int(n) else (int(n)+1)**2
    rectangle=int(n)*(int(n)+1)
    if len(res)>rectangle:
        rectangle=(rectangle*(int(n)+2))//int(n)
    if square<rectangle:
        length=int(square**0.5)
        return " ".join("".join(" " if i+j*length>=len(res) else res[i+j*length] for j in range(length)) for i in range(length))
    width=rectangle//(int(n)+1)
    height=rectangle//width
    return " ".join("".join(" " if i+j*max(width, height)>=len(res) else res[i+j*max(width, height)] for j in range(min(width, height))) for i in range(max(width, height)))