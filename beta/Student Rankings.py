def post_grades(students):
    res=[]
    for i in students:
        arr=i.split(" - ")
        score=round(sum(float(j) for j in arr[-1].split())/(arr[-1].count(" ")+1), 2)
        res.append((arr[0], score))
    res.sort(key=lambda x: (-x[-1]))
    return res