def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number and step > 0:
        return 0
    elif begin_number < end_number and step < 0:
        return 0
    elif begin_number == end_number:
        return begin_number
    count = (end_number-begin_number)//step
    return (begin_number+count*step+begin_number)*(count+1)//2
