class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def push(head, data):
    if not head:
        return Node(data)
    temp=Node(data)
    temp.next=head
    return temp
def build_one_two_three():
    list=push(None, 3)
    list=push(list, 2)
    list=push(list, 1)
    return list