def nba_cup(result_sheet, to_find):
    if not to_find:
        return ""
    elif "." in result_sheet:
        return "Error(float number):New York Knicks 101.12 Atlanta Hawks 112"
    dict = {}
    temp = result_sheet.split(",")
    for i in temp:
        teams = i.split()
        for i, j in enumerate(teams):
            if j.isdigit():
                index = i
                break
        team1 = " ".join(teams[:index])
        team2 = " ".join(teams[index+1:-1])
        score1 = int(teams[index])
        score2 = int(teams[-1])
        if not dict.get(team1, None):
            dict[team1] = {"W": 0, "D": 0, "L": 0,
                           "Scored": 0, "Conceded": 0, "Points": 0}
        if not dict.get(team2, None):
            dict[team2] = {"W": 0, "D": 0, "L": 0,
                           "Scored": 0, "Conceded": 0, "Points": 0}
        dict[team1]["Scored"] += score1
        dict[team1]["Conceded"] += score2
        dict[team2]["Scored"] += score2
        dict[team2]["Conceded"] += score1
        if score1 > score2:
            dict[team1]["W"] += 1
            dict[team2]["L"] += 1
            dict[team1]["Points"] += 3
        elif score1 == score2:
            dict[team1]["D"] += 1
            dict[team2]["D"] += 1
            dict[team1]["Points"] += 1
            dict[team2]["Points"] += 1
        else:
            dict[team2]["W"] += 1
            dict[team2]["Points"] += 3
            dict[team1]["L"] += 1
    try:
        res = []
        for i, j in dict[to_find].items():
            res.append(f"{i}={j}")
        return to_find+":"+";".join(res)
    except:
        return f"{to_find}:This team didn't play!"
