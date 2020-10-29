def shoot(results):
    scores=[0,0]
    for i in results:
        mark=2 if i[1] else 1
        scores[0]+=sum(mark for j in i[0]["P1"] if j=="O")
        scores[1]+=sum(mark for j in i[0]["P2"] if j=="O")
    return 'Pete Wins!' if scores[1]>scores[0] else 'Phil Wins!' if scores[1]<scores[0] else 'Draw!'