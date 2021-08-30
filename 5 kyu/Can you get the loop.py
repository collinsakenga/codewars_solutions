def loop_size(node):
    dict={}
    index=0
    while node:
        try:
            return index-dict[node]
        except:
            dict[node]=index
        node=node.next
        index+=1