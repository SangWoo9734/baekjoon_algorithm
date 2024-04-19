import sys

input = sys.stdin.readline

N = int(input())

dp = [ 0 ] * ( N + 1 )
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
  dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

print(dp[N])


  # dp(i) =  dp(1) + dp(i - 1)
# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 5
# 5 -> 8

# dp[5]

# dp [3]
# 2  1 1 1
# 2  1 2
# 2  2 1

# dp[4]
# 1   1 1 1 1
# 1   1 1 2
# 1   1 2 1
# 1   2 1 1
# 1   2 2



