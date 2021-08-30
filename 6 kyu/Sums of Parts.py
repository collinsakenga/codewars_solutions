def parts_sums(ls):
    record=sum(ls)
    result=[record]
    total=0
    for i in ls:
        total+=i
        result.append(record-total)
    return result