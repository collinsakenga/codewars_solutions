def front_back_split(source, front, back):
    if not source or not front or not back or not source.next:
        raise Exception()
    length=0
    temp=source
    while source:
        length+=1
        source=source.next
    for i in range(length//2+length%2):
        if i==0:
            front.data=temp.data
        else:
            front.next=Node(temp.data)
            front=front.next
        temp=temp.next
    for i in range(length//2):
        if i==0:
            back.data=temp.data
        else:
            back.next=Node(temp.data)
            back=back.next
        temp=temp.next 