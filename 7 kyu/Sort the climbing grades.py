def sort_grades(lst):
    return sorted(lst, key=lambda x: (-1 if x[-1]=="B" else int(x[1:-1])*2+1 if x[-1]=="+" else int(x[1:])*2))