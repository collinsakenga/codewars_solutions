def find_missing_number(numbers):
    if not numbers: return 1
    m=max(numbers)
    temp=sum(numbers)
    if m*(m+1)//2==temp:
        return m+1
    return m*(m+1)//2-temp