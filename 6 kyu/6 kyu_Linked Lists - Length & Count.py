class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    if not node:
        return 0
    length=1
    while node.next:
        node=node.next
        length+=1
    return length
  
def count(node, data):
    if not node:
        return 0
    count=1 if node.data==data else 0
    while node.next:
        node=node.next
        if node.data==data:
            count+=1
    return count