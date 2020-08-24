def sum_of_intervals(intervals):
    intervals = sorted([list(i) for i in intervals], key=lambda x: x[0])
    delete = 0
    for _ in range(len(intervals)-1):
        if intervals[delete+1][0] <= intervals[delete][1]:
            if intervals[delete][1] < intervals[delete+1][1]:
                intervals[delete][1] = intervals[delete+1][1]
            intervals.pop(delete+1)
            delete -= 1
        delete += 1
    print(intervals)
    return sum(x[1]-x[0] for x in intervals)
