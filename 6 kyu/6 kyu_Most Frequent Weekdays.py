def most_frequent_days(year):
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    if year == 2000:
        return ['Saturday', 'Sunday']
    check = 2000
    if year > check:
        day = 6
        while check < year:
            check += 1
            day += 2 if leap(check) else 1
        if day % 7 == 0:
            return [days[(day) % 7], days[(day-1) % 7]] if leap(year) else [days[day % 7]]
        return [days[(day-1) % 7], days[(day) % 7]] if leap(year) else [days[day % 7]]
    elif year < check:
        day = 5
        while check > year:
            check -= 1
            day -= 2 if leap(check) else 1
        if (day+1) % 7 == 0:
            return [days[(day+1) % 7], days[day % 7]] if leap(year) else [days[day % 7]]
        return [days[day % 7], days[(day+1) % 7]] if leap(year) else [days[day % 7]]


def leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False
