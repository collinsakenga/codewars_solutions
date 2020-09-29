def index_of(words, target):
    start = 0
    end = len(words)-1
    while start <= end:
        mid = (start+end)//2
        if target == words[mid]:
            return mid
        if len(target) > len(words[mid]):
            start = mid+1
        elif len(target) < len(words[mid]):
            end = mid-1
        else:
            comp_target = count_upper(target)
            comp_mid = count_upper(words[mid])
            if comp_target < comp_mid:
                start = mid+1
            elif comp_target > comp_mid:
                end = mid-1
            else:
                if target > words[mid]:
                    start = mid+1
                else:
                    end = mid-1


def count_upper(s):
    total = 0
    for i in s:
        if i.isupper():
            total += 1
    return total
