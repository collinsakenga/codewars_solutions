def bulk(arr):
    total = 0
    protein = 0
    for i in arr:
        for j in i.split(", "):
            index = next(index for index, char in enumerate(j)
                         if char.isalpha())
            total += calories(food[j.split()[1]], int(j[:index]))
            protein += food[j.split()[1]][0]*int(j[:index])/100
    total = total if int(total) != total else int(total)
    protein = protein if int(protein) != protein else int(protein)
    return f"Total proteins: {protein} grams, Total calories: {total}"


def calories(arr, gram):
    return (4*arr[0]+4*arr[1]+9*arr[2])*gram/100