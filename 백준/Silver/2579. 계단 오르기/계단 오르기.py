
n = int(input())

def solution(n):
    stairs = [0 for _ in range(301)]
    dp = [0 for _ in range(301)]

    for i in range(1, n+1):
        stairs[i] = int(input())

    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n+1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    print(dp[n])
    
solution(n)
