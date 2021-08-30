# Exclude 'y' from vowels since it can't make up its mind if it's a vowel
vowels = 'aeiou'

def find_solutions(words):
    """Searches for solutions to the game returning a list of all solutions."""
    temp=[]
    solutions = []
    temp2=[]
    for i in words:
        if i in temp2:
            continue
        for j, char in enumerate(i):
            if char in vowels:
                for k in vowels:
                    if not ((i[:j]+k+i[j+1:]) in words):
                        temp=[]
                        break
                    temp.append(i[:j]+k+i[j+1:])
            if temp and (temp not in solutions):
                solutions.append(temp)
                temp2=[j for i in solutions for j in i]
                temp=[]
                break
    return solutions