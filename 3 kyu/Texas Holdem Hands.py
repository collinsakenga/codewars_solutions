from collections import defaultdict
class poker:
    def __init__(self, hands):
        self.hands=self.classify(hands)
        self.numbers_table=defaultdict(int)
        self.types_table=defaultdict(int)
        for type, number in self.hands:
            self.numbers_table[number]+=1
            self.types_table[type]+=1
        self.straight=self.three=None
    def evaluate(self):
        for index, func in enumerate((self.straight_flush, self.four, self.three_pair, self.flush, self.get_straight, self.three_single, self.pairs)):
            result=func()
            if result: return index++(len(result)==4), result
        return 8, tuple(sorted(self.numbers_table.keys()))[::-1][:5]
    def classify(self, hands):
        # A=12, K=11, ... 2=0
        types={type:index for index, type in enumerate("♦♣♥♠")}
        numbers={number:index for index, number in enumerate(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))}
        return {(types[card[-1]], numbers[card[:-1]]) for card in hands}
    def straight_flush(self):
        cur=sum(+(num in self.numbers_table) for num in range(12, 12-5, -1))
        for n in range(12-5, -2, -1):
            if cur==5: 
                combo=next((tuple(range(n+1, n+5+1)) for type in range(4) if all(card in self.hands for card in tuple((type, num) for num in range(n+1, n+5+1)))), None)
                if combo: return combo[::-1]
                elif self.straight is None: self.straight=tuple(range(n+1, n+5+1))[::-1]
            cur+=+(n in self.numbers_table)-+(n+5 in self.numbers_table)
    def get_straight(self): return self.straight
    def four(self):
        val=max((num for num, count in self.numbers_table.items() if count==4), default=float("-inf"))
        if val>=0: return (val, max(num for num in self.numbers_table.keys() if num!=val))
    def three_pair(self):
        val=max((num for num, count in self.numbers_table.items() if count==3), default=float("-inf"))
        if val>=0: 
            self.three=val
            return (val, ans) if (ans:=max((num for num, count in self.numbers_table.items() if num!=val and count>1), default=float("-inf")))>=0 else None
    def flush(self):
        val=max((num for num, count in self.types_table.items() if count>=5), default=float("-inf"))
        if val>=0: return tuple(sorted(num for type, num in self.hands if type==val))[::-1][:5]
    def three_single(self):
        if not self.three is None: return (self.three,)+tuple(sorted(num for num, count in self.numbers_table.items() if num!=self.three))[-2:][::-1]
    def pairs(self):
        pair=tuple(sorted(num for num, count in self.numbers_table.items() if count==2))[::-1]
        if len(pair)==1: return (pair[0],)+tuple(sorted(num for num in self.numbers_table.keys() if num!=pair[0]))[::-1][:3]
        elif len(pair)==2: return (pair[0], pair[1])+(max(num for num in self.numbers_table.keys() if num!=pair[0] and num!=pair[1]),)
def hand(hole_cards, community_cards, trans={index:number for index, number in enumerate(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"))}):
    res=poker(hole_cards+community_cards)
    type, ans=res.evaluate()
    return ("straight-flush", "four-of-a-kind", "full house", "flush", "straight", "three-of-a-kind", "two pair", "pair", "nothing")[type], [trans[num] for num in ans]