# have a jolly good time sleuthing!
def boston_breakout(robberies):
    return [(j-500)/robberies[i] for i,j in enumerate(robberies[1:])]