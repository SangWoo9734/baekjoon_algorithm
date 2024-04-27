import sys

input = sys.stdin.readline

N = int(input())

dp = [ [ 1 ] * 10 + [ 0 ] ] + [ [ 1 ] + [ 0 ] * 10 for _ in range(N - 1) ]

for n in range(1, N):
  for i in range(0, 10):
    if i == 0 :
      dp[n][i] = dp[n -1][i + 1]
    else:
      dp[n][i] = (dp[n - 1][i - 1] + dp[n -1][i + 1]) 



print((sum(dp[N - 1]) - dp[N-1][0]) % 1000000000)
# print(dp[N - 1])
# 1 -> 1,      2
# 2 -> 10, 12, 21, 23, ... 98 -> 17

