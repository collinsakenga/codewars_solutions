def cakes(recipe, available):
    total=0
    comp=10000000
    for i in recipe.keys():
        try:
            total=available[i]//recipe[i]
        except:
            return 0
        if total<comp:
            comp=total
    return comp