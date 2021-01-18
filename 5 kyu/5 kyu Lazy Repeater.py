def make_looper(string):
    global index
    index=-1
    def rotate():
        global index
        index+=1
        return string[(index)%len(string)]
    return rotate