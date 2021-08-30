def simple_assembler(program):
    res={}
    index=0
    while index<len(program):
        command=program[index].split(" ")
        if command[0]=="mov":
            try:
                res[command[1]]=int(command[2])
            except:
                res[command[1]]=res[command[2]]
        elif command[0]=="inc":
            res[command[1]]+=1
        elif command[0]=="dec":
            res[command[1]]-=1
        else:
            if (command[1]!="0" and res.get(command[1], -1)!=0):
                index+=int(command[2])-1
        index+=1
    return res