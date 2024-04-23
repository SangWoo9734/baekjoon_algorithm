import sys

input = sys.stdin.readline

N = int(input())

P = [0] + list(map(int, input().split()))

dp = [ 0 ] * ( N + 1 )

for i in range(N + 1):
  if dp[i] == 0:
    dp[i] = P[i]

  for j in range(N + 1):
    if i + j <= N:
      if dp[i] + P[j] < dp[i + j] or dp[i + j] == 0:
        dp[i + j] = dp[i] + P[j]

  # print(dp)

print(dp[N])