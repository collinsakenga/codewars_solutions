from collections import Counter
def get_winner(ballots):
    most_vote=Counter(ballots).most_common(1)[0]
    return None if most_vote[1]<=len(ballots)//2 else most_vote[0]