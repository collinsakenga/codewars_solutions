def interpreter(tape):
    res=[0]
    s=""
    index=0
    while index<len(tape):
        char=tape[index]
        if char=="^":
            res.pop()
            index+=1
        elif char=="!":
            res.append(0)
            index+=1
        elif char=="+":
            res[-1]=(res[-1]+1)%256
            index+=1
        elif char=="-":
            res[-1]=(res[-1]-1)%256
            index+=1
        elif char=="*":
            s+=chr(res[-1])
            index+=1
        elif char=="[":
            if res[-1]==0:
                flag=True
                while index<len(tape):
                    if flag==False and tape[index]!="]":
                        break
                    flag=False if tape[index]=="]" else True
                    index+=1
            else:
                index+=1
        elif char=="]":
            if res[-1]!=0:
                while index>=0 and tape[index]!="[":
                    index-=1
            else:
                index+=1
        else:
            index+=1
    return s