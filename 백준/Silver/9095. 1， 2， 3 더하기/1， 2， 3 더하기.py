import sys 
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]

maxi = (max(nums) + 1)
dp = [0] * maxi
dp[1], dp[2], dp[3] = 1, 2, 4

for idx in range(4, maxi):
    dp[idx] = dp[idx-1] + dp[idx-2] + dp[idx-3]

for num in nums:
    print(dp[num])