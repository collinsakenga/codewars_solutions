def my_very_own_split(string, delimiter = None):    
    temp=""
    if delimiter=="":
        raise error("Expected an error when empty delimiter!")
    elif delimiter==None:
        for i in string+" ":
            if i=="\t" or i==" ":
                if temp:
                    yield temp
                    temp=""
                continue
            temp+=i
    else:
        for i in string:
            if temp.endswith(delimiter):
                yield temp.replace(delimiter, "")
                temp=i
            else:
                temp+=i 
        yield temp.replace(delimiter, "")
        if string.endswith(delimiter):
            yield ""  