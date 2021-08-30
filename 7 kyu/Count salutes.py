def count_salutes(hallway):
    count=hallway.count("<")
    total=0
    for i in hallway:
        count-=i=="<"
        if i==">":
            total+=count*2
    return total
    