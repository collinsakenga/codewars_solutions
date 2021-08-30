class Trie:

    def __init__(self):
        self.trie={}
        

    def insert(self, word: str) -> None:
        cur=self.trie
        for i in word:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
    def get_trie(self):
        return self.trie
def phone_number(numbers):
    tree=Trie()
    for i in numbers:
        tree.insert(i)
    ans=tree.get_trie()
    print(helper(ans))
    return helper(ans)
def helper(tree):
    if isinstance(tree, str):
        return 1
    return len(tree)+sum(helper(i) for i in tree.values())