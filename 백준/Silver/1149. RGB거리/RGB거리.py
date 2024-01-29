n = int(input())
datas = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)] 

answer = 0
prev = -1

dp[0] = datas[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + datas[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + datas[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + datas[i][2]

print(min(dp[-1]))