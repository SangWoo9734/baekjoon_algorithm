import sys

input = sys.stdin.readline


N = int(input())

color_cost = [ [0 , 0, 0] ] + [ list(map(int, input().split())) for _ in range(N) ]

dp = [ [ 0, 0, 0 ] for _ in range(N + 1) ]

dp[1] = color_cost[1]

for i in range(2, N + 1):
  r, g, b = color_cost[i]
  dp[i][0] = r + min(dp[i - 1][1], dp[i - 1][2])
  dp[i][1] = g + min(dp[i - 1][0], dp[i - 1][2])
  dp[i][2] = b + min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N]))
