import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [ [1 for _ in range(N + 1)] for _ in range(K + 1)]

# 0 = 1
# 1 = 1
# 2 = 2 / 1 + 1
# 3 = 2 + 1 ( dp[i - 2] ), 1 + 2, 1 + 1 + 1 /dp[i - 1] + 3 (1)
# 4 = 1 + 3 / 2 + 2, 1 + 1 + 2 / 2 + 1 + 1, 1 + 2 + 1, 1 + 1 + 1 + 1  + 4 (1)

# print(*dp, sep='\n')

for i in range(2, K + 1):
  for j in range(1, N + 1):
    dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000000


print(dp[K][N])


# print('\n')

# print(*dp, sep='\n')