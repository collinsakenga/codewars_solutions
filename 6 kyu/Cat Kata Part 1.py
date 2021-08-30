from itertools import combinations
def peaceful_yard(yard, min_distance):
    dict={}
    for i,j in enumerate(yard):
        for k,l in enumerate(j):
            if l!="-":
                dict[l]=[i, k]
    if len(dict)<=1:
        return True
    for i in combinations(dict, 2):
        temp1=dict[i[0]]
        temp2=dict[i[1]]
        distance=(abs(temp2[0]-temp1[0])**2+abs(temp2[1]-temp1[1])**2)**0.5
        if distance<min_distance:
            return False
    return True