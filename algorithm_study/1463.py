import sys

input = sys.stdin.readline

N = int(input())

# MAX = N + 1

# 피보나치 느낌으로?
# dp = [ 1, 0 ] + [ MAX ] * (N - 1)

# value = 0

# # bottom up
# for i in range(1, N + 1):
#   if i + 1 <= N :
#     dp[i + 1] = dp[i] + 1 if dp[i] + 1 < dp[i + 1] else dp[i + 1]

#   if i * 2 <= N :
#     dp[i * 2] = dp[i] + 1 if dp[i] + 1 < dp[i * 2] else dp[i * 2]

#   if i * 3 <= N :
#     dp[i * 3] = dp[i] + 1 if dp[i] + 1 < dp[i * 3] else dp[i * 3]


# print(dp[N])


# top down
dp = { 1 : 0, 2 : 1 }


def func(n):
    if n in dp:
        return dp[n]

    if n % 3 == 0 and n % 2 == 0:
        dp[n] = min(func(n // 3), func(n // 2)) + 1
    elif n % 3 == 0:
        dp[n] = min(func(n // 3), func(n - 1)) + 1
    elif n % 2 == 0:
        dp[n] = min(func(n // 2), func(n - 1)) + 1
    else:
        dp[n] = func(n - 1) + 1

    return dp[n]


print(func(N))
