class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    if not head:
        return Node(data)
    elif not index:
        res=Node(data)
        res.next=head
        return res    
    else:
        temp=head
        res=Node(data)
        for i in range(index-1):
            head=head.next
            if not head:
                raise Exception()
        res.next=head.next
        head.next=res 
        return temp