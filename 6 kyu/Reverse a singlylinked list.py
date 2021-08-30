def reverse_list(node):
    res=[]
    while node:
        res.append(node.value)
        node=node.next
    return make_linked_list(res[::-1])