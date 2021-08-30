from struct import *
def patch_data(string):
    index, res=0, ""
    while index<len(string):
        endian=unpack("<h", bytes(string[index:index+2], 'utf-8'))
        num=sum(16**(len(endian)-i-1)*j for i,j in enumerate(endian))
        name="".join(i for i in string[index+2:index+2+num])
        res+=string[index:index+2]+name+"\xf4\x01"
        index+=num+4
    return res