from collections import Counter
def count_mentioned(con,names):
    con=con.lower()
    res=[con.count(i.lower()) for i in names]
    return res if res else None