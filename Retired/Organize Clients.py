def organize(client):
    res={}
    for i in client:
        if isinstance(i, bool):
            res['Occupation']=i
        elif isinstance(i, int):
            res['Age']=i
        elif isinstance(i, tuple):
            res['Hobbies']=i
        elif isinstance(i, str):
            res['Name']=i
    return res