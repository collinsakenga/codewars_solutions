from collections import Counter
def directions(goal):
    check=Counter(goal)
    horizontal=check["E"]-check["W"]
    vertical=check["N"]-check["S"]
    return sorted(abs(horizontal)*["E" if horizontal >=0 else "W"]+abs(vertical)*["N" if vertical >=0 else "S"], key=lambda x: compare(x))
def compare(s):
    return ["N","S","E","W"].index(s)