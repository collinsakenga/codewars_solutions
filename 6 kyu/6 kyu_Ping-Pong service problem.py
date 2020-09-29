def service(score):
    first = int(score.split(":")[0])
    second = int(score.split(":")[1])
    if first < 20 and second < 20:
        return "first" if (first+second)//5 % 2 == 0 else "second"
    return "first" if (first+second-40)//2 % 2 == 0 else "second"
