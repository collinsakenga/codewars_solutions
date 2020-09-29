def leaderboard_sort(leaderboard, changes):
    for i in changes:
        sign = i.split()[1][0]
        num = int(i.split()[1][1:])
        name = i.split()[0]
        index = leaderboard.index(name)
        if sign == "+":
            for j in range(num):
                temp = leaderboard[index-j-1]
                leaderboard[index-j] = temp
                leaderboard[index-j-1] = name
        elif sign == "-":
            for j in range(num):
                temp = leaderboard[index+j+1]
                leaderboard[index+j] = temp
                leaderboard[index+j+1] = name
    return leaderboard
