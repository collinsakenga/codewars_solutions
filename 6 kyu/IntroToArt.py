def get_w(height):
    if height<=1:
        return []
    len_col=(1+4*(height-1))
    append_string=""
    result=[]
    count=1
    for row in range(1,height+1):
        for col in range(1,len_col+1):
            if col-count==0:
                append_string+="*"
            elif col+count-1==len_col:
                append_string+="*"
            elif col+row==height*2:
                append_string+="*"
            elif col+row==height*2+2*count-2:
                append_string+="*"
            else:
                append_string+=" "
        count+=1
        result.append(append_string)           
        append_string=""
    return result