def encrypt_this(text):
    text=text.split()
    append_result=[]
    for word in text:
        append_list=list(word)
        append_list[0]=str(ord(append_list[0]))
        if len(append_list)>1:
            temp=append_list[1]
            append_list[1]=append_list[-1]
            append_list[-1]=temp
        append_result.append("".join(append_list))
    return " ".join(append_result)