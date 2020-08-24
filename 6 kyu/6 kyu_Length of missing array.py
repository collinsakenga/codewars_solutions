def get_length_of_missing_array(array_of_arrays):
    comp = []
    for i in array_of_arrays:
        if i:
            comp.append(len(i))
        elif not i:
            return 0
    comp.sort()
    for i in range(0, len(comp)-1):
        if comp[i+1]-comp[i] != 1:
            return (comp[i+1]+comp[i])//2
    return 0
