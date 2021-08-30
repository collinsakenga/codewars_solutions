def interpreter(tape, array): # Tape is given as a string and array is given as a string.
    pos=index=0
    res=list(array)
    while pos<len(res):
        if tape[index]=="1":
            res[pos]="1" if res[pos]=="0" else "0"
        else:
            pos+=1
        index=(index+1)%len(tape)
    return "".join(res)
    