limit_range = []
solution = "112123123412345123456123456712345678123456789"


def solve(n):
    if n <= 45:
        return int(solution[n-1])
    if not limit_range:
        limit_range.append(9)
        for i in range(2, 10):
            limit_range.append(9*10**(i-1)*i+limit_range[-1])
    upper_limit = 45
    index = 0
    while upper_limit < n:
        lower_limit = upper_limit
        num = 10**(index+2)-10**(index+1)
        upper_limit = upper_limit + \
            limit_range[index]*num+(index+2)*num*(num+1)//2
        index += 1
    low = 10**index
    high = 10**(index+1)-1
    decrement = low
    while low <= high:
        mid = (low+high)//2
        multiply = mid-decrement
        compare = lower_limit+limit_range[index-1] * \
            multiply+(index+1)*multiply*(multiply+1)//2
        compare_plus_one = lower_limit + \
            limit_range[index-1]*(multiply+1)+(index+1) * \
            (multiply+1)*(multiply+2)//2
        if n >= compare and n < compare_plus_one:
            break
        elif n > compare:
            low = mid+1
        elif n < compare:
            high = mid-1
    flag = n-compare
    if flag <= 9 and flag >= 1:
        return flag
    elif flag == 0:
        return int(str(mid-1)[-1])
    index2 = 0
    while True:
        if limit_range[index2+1] > flag:
            break
        index2 += 1
    final = limit_range[index2]
    number_of_n = 10**(index2+1)-1+(flag-final)//(index2+2)
    diff = (flag-final)-(flag-final)//(index2+2)*(index2+2)
    if diff == 0:
        return int(str(number_of_n)[-1])
    return int(str(number_of_n+1)[diff-1])