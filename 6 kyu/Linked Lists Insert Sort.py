class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_sort(head):
    res=None
    while head:
        res=sorted_insert(res, head.data)
        head=head.next
    return res