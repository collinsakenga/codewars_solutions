def digit_derby(num_to_sum, range_end):
    num=abs(sum(i for i in range(range_end+1) if sum(int(j) for j in str(i))==num_to_sum)-100000)
    if num==100000:
        return "No numbers"
    return num