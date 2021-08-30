def is_a_valid_message(message):
    index=0
    while index<len(message):
        index2=next((i for i,j in enumerate(message[index:]) if not j.isdigit()), 0)+index
        if index==index2:
            return False
        index3=next((i for i,j in enumerate(message[index2:]) if j.isdigit()), len(message)-index2)+index2
        if message[index:index2].startswith("0") or index2+int(message[index:index2])!=index3:
            return False
        index=index3 
    return True