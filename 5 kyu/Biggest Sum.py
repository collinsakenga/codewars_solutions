def find_sum(m):
    dp=[[None]*len(m[i]) for i in range(len(m))]
    return helper(m, len(m)-1, len(m)-1, dp)
def helper(arr, y, x, dp):
    for i in range(y,-1, -1):
        for j in range(x, -1, -1):
            if i==y and j==x:
                dp[i][j]=arr[i][j]
            elif i==y:
                dp[i][j]=arr[i][j]+dp[i][j+1]
            elif j==x:
                dp[i][j]=arr[i][j]+dp[i+1][j]
            else:
                dp[i][j]=arr[i][j]+max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]