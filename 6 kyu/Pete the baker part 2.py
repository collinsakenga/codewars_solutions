def get_missing_ingredients(recipe, added):
    times=0
    temp=recipe.copy()
    temp2=added.copy()
    for i in added:
        try:
            times=max(times, temp2[i]//temp[i]) if temp2[i]%temp[i]==0 else max(times, temp2[i]//temp[i]+1)
        except:
            pass
    for i in temp:
        try:
            if times:
                temp[i]=temp[i]*times-temp2[i]
            else:
                temp[i]-=temp2[i]
        except:
            if times: temp[i]*=times
    return {a: b for a,b in temp.items() if b!=0}