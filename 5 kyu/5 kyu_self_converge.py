def self_converge(number):
    memo, count, num, digits=set(), 0, number, len(str(number))
    while True:
        temp="".join(sorted(str(num)))
        maximum=temp[::-1].ljust(digits, "0")
        minimum=temp.rjust(digits, "0")
        num=int(maximum)-int(minimum)
        count+=1
        if num in memo:
            break
        memo.add(num)
    return -1 if num==0 else count