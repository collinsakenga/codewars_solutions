def count_duplicates(name,age,height):
    return len(name)-len(({*zip(name,age,height)}))