class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return None
    elif not head.next:
        return head
    temp=head
    while head.next:
        if head.data==head.next.data:
            head.next=head.next.next
        else:
            head=head.next
    return temp