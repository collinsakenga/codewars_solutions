def guess_gifts(wishlist, presents): 
    res=[j["name"] for i in presents for index,j in enumerate(wishlist) if all(k in j and v==j[k] for k,v in i.items())]
    return {j: None for j in res}.keys()