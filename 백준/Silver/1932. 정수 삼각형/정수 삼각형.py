n = int(input())
datas = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0 for _ in datas[i]] for i in range(n)]
dp[0] = datas[0]

for i in range(1, n):
    size = len(datas[i])
    for j in range(size):
        if j == 0: dp[i][j] = dp[i-1][0] + datas[i][j]
        elif j == (size - 1): dp[i][j] = dp[i-1][-1] + datas[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + datas[i][j]

print(max(dp[-1]))