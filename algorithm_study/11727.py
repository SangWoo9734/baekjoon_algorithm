# import sys

# input = sys.stdin.readline

# N = int(input())

# dp = [ 0 ] * ( N + 1 )
# dp[0] = 1
# dp[1] = 1

# for i in range(2, N + 1):
#   dp[i] = (dp[i - 1] +  2 * dp[i - 2]) % 10007

# print(dp[N])

N = int(input())

a = b = 1

for _ in range(N - 1):
  a, b = b, (a * 2 + b) % 10007

print(b)

  # dp(i) =  dp(i -  1) + 2 * dp(i - 2)
# 1 -> 1
# 2 -> 3
# 3 -> 5
# 4 -> 11
# 5 -> 21

# dp[5]

# dp [3]
# 2a  1 1 1
# 2b  1 1 1

# 2a  1 2a
# 2a  1 2b

# 2b  1 2a
# 2b  1 2b

# 2a  2a 1
# 2a  2b 1

# 2b  2a 1
# 2b  2b 1



# dp[5] -> dp[4]
# 1   1 1 1 1
# 1   1 1 2
# 1   1 2 1
# 1   2 1 1
# 1   2 2

# dp[4]
# 1 1 1 1
# 1 1 2a
# 1 1 2b
# 1 2a 1
# 1 2b 1
# 2a 1 1
# 2b 1 1
# 2a 2a
# 2a 2b
# 2b 2a
# 2b 2b