class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    if not listA and not listB:
        return None
    elif not listA:
        return listB
    elif not listB:
        return listA
    res=listA
    while listA.next:
        listA=listA.next
    listA.next=listB
    return res
    