def alternate_sort(l):
    temp=sorted(l, key=lambda x: abs(x))
    positive, negative=[i for i in temp if i>=0], [i for i in temp if i<0]
    left=sum([[i,j] for (i,j) in zip(negative, positive)], [])
    right=positive[-(len(positive)-len(negative)):] if len(positive)>len(negative) else negative[-(len(negative)-len(positive)):] if len(positive)<len(negative) else []
    return left+right