def namelist(names):
    res=[i["name"] for i in names]
    if not res:
        return ""
    return res[0] if len(res)==1 else ", ".join(res[:-1])+" & "+res[-1]