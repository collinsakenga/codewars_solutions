class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
def sorted_merge(first, second):
    if not first and not second:
        return None
    elif not first:
        return second
    elif not second:
        return first
    res=final=None
    while first and second:
        if first.data>second.data:
            if not res:
                res=Node(second.data)
                final=res
            else:
                res.next=Node(second.data)
                res=res.next
            second=second.next
        else:
            if not res:
                res=Node(first.data)
                final=res
            else:
                res.next=Node(first.data)
                res=res.next
            first=first.next
    while first:
        res.next=Node(first.data)
        res=res.next
        first=first.next
    while second:
        res.next=Node(second.data)
        res=res.next
        second=second.next
    return final