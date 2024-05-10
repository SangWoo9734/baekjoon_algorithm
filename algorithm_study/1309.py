import sys

input = sys.stdin.readline

N = int(input())

dp = [ 0 ] * ( N + 1 )

dp[0] = 1
dp[1] = 3

for n in range(2, N + 1):
  dp[n] = (2 * dp[n - 1] + dp[n - 2]) % 9901


print(dp[N])