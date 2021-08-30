""" For your information:
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
"""

def shuffle_merge(first, second):
    if not first:
        return second
    elif not second:
        return first
    res=None
    final=None
    while first or second:
        if first:
            if not res:
                res=Node(first.data)
                final=res
            else:
                temp=Node(first.data)
                res.next=temp
                res=res.next
            first=first.next
        if second:
            temp=Node(second.data)
            res.next=temp
            res=res.next
            second=second.next
    return final