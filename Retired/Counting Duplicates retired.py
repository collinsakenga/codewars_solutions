def countDuplicates(name,age,height):
    return len(name)-len({(i, j, k) for i,j,k in zip(name,age,height)})