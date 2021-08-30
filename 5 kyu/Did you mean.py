class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
        length, ans=float("inf"), ""
        for i in self.words:
            distance=self.distance(i, term)
            if distance<length:
                length=distance
                ans=i
        return ans
    def distance(self, s1, s2):
        dp=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    if s1[i-1]==s2[j-1]:
                        dp[i][j]=dp[i-1][j-1]
                    else:
                        dp[i][j]=min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        return dp[-1][-1]