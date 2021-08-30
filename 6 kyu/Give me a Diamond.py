def diamond(n):
    if n%2==0 or n<0:
        return None
    else:
        value=int((n-1)/2)
        count=0
        append_string=""
        comp=value
        while count<n:
            if count<value:
                for space in range(value-count):
                    append_string+=" "
                for star in range(2*(count+1)-1):
                    append_string+="*"
            elif count>value:
                for space in range(count-value):
                    append_string+=" "
                for star in range(2*(comp)-1):
                    append_string+="*"
                comp-=1
            else:
                for star in range(n):
                    append_string+="*"
            count+=1
            append_string+="\n"
        return append_string
           