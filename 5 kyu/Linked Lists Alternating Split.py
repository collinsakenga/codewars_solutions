class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise Exception()
    first=second=res1=res2=None
    while True:
        if not head: break
        temp=Node(head.data)
        if not first:
            first=temp
            res1=first
        else:
            first.next=temp
            first=first.next
        head=head.next        
        if not head: break
        temp2=Node(head.data)
        if not second:
            second=temp2
            res2=second
        else:
            second.next=temp2
            second=second.next
        head=head.next
    return Context(res1, res2)