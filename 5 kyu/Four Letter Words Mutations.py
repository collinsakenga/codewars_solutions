def mutations(alice, bob, word, first):
    table1={i:j for i, j in enumerate(alice) if len(j)==len(set(j))}
    table2={i:j for i, j in enumerate(bob) if len(j)==len(set(j))}
    if first:
        table1, table2=table2, table1
    visited={word}
    index1, index2=0, 0
    if not first:
        while table1 and table2:
            index1=next((i for i,j in table1.items() if j not in visited and sum(k!=l for k,l in zip(j, word))==1), -1)
            if index1>=0:
                word=table1[index1]
                visited.add(word)
                table1.pop(index1) 
            if first and index1>=0 and index2<0:      
                return 0
            if first and index2>=0 and index1<0:
                return 1
            first=True
            index2=next((i for i,j in table2.items() if j not in visited and sum(k!=l for k,l in zip(j, word))==1), -1)
            if index2>=0:
                word=table2[index2]
                visited.add(word)
                table2.pop(index2)
            if index2>=0 and index1<0:
                return 1
            if index1>=0 and index2<0:
                return 0
            if index1<0 and index2<0:
                return -1
    else: 
        while table1 and table2:
            index1=next((i for i,j in table1.items() if j not in visited and sum(k!=l for k,l in zip(j, word))==1), -1)
            if index1>=0:
                word=table1[index1]
                visited.add(word)
                table1.pop(index1) 
            if not first and index1>=0 and index2<0:      
                return 1
            if not first and index2>=0 and index1<0:
                return 0
            first=False
            index2=next((i for i,j in table2.items() if j not in visited and sum(k!=l for k,l in zip(j, word))==1), -1)
            if index2>=0:
                word=table2[index2]
                visited.add(word)
                table2.pop(index2)
            if index2>=0 and index1<0:
                return 0
            if index1>=0 and index2<0:
                return 1
            if index1<0 and index2<0:
                return -1