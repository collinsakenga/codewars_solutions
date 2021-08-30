class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    if not node or index<0:
        raise exception()
    for i in range(index):
        node=node.next
        if not node:
            raise exception()
    return node
  