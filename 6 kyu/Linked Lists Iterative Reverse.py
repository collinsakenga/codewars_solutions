class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    temp=[]
    temp2=head
    while temp2:
        temp.append(temp2.data)
        temp2=temp2.next
    while head:
        head.data=temp[-1]
        temp.pop()
        head=head.next