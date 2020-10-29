def get_participants(handshakes):
    count=0
    total=1
    increment=1
    while count<handshakes:
        total+=1
        count+=increment
        increment+=1
    return total