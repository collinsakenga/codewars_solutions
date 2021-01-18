res=[]
data=None
def search_k_from_end(linked_list, k):
    global res, data
    if not data:
        data=linked_list
        while linked_list.head:
            res.append(linked_list.head.data)
            linked_list.head=linked_list.head.next
        try:
            return res[-k]
        except:
            return None
    elif data!=linked_list:
        data=linked_list
        res=[]
        while linked_list.head:
            res.append(linked_list.head.data)
            linked_list.head=linked_list.head.next
        try:
            return res[-k]
        except:
            return None
    else:
        try:
            return res[-k]
        except:
            return None