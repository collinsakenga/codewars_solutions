good_side=[1,2,3,3,4,10]
bad_side=[1,2,2,2,3,5,10]
def goodVsEvil(good, evil):
    return "Battle Result: Good triumphs over Evil" if sum(good_side[i]*int(j) for i,j in enumerate(good.split())) > sum(bad_side[i]*int(j) for i,j in enumerate(evil.split())) else "Battle Result: Evil eradicates all trace of Good" if sum(good_side[i]*int(j) for i,j in enumerate(good.split())) < sum(bad_side[i]*int(j) for i,j in enumerate(evil.split())) else "Battle Result: No victor on this battle field" 