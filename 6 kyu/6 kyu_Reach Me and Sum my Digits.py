def sumDig_nthTerm(initVal, patternL, nthTerm):
    return sum(int(i) for i in str(initVal+(sum(patternL)*((nthTerm-1)//len(patternL)))+sum(patternL[:(nthTerm-1) % len(patternL)])))
