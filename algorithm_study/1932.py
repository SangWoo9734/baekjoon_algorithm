import sys

input = sys.stdin.readline

n = int(input())

tri = [ list(map(int, input().split())) for _ in range(n) ] 

dp = [ [0 for _ in range(i)] for i in range(1, n + 1) ]
dp[0][0] = tri[0][0]

for i in range(1, n):
  for j in range(len(tri[i])):
    
    left = 0
    right = 0

    if j != 0:
      left = dp[i-1][j-1] + tri[i][j]
    if len(dp[i-1]) != j:
      right = dp[i-1][j] + tri[i][j]

    dp[i][j] = max(right, left, dp[i][j])

print(max(dp[-1]))