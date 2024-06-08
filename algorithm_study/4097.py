import sys

input = sys.stdin.readline

# while True:
#   N = int(input())

#   if N == 0:
#     break

#   P = [0] + [ int(input()) for _ in range(N) ]

#   dp = [ [0 for _ in range(N + 1)] for _ in range(N + 1) ]

#   e = -300000000

#   for i in range(1, N + 1):
#     dp[i][i] = P[i]
#     if e < dp[i][i]:
#       e = dp[i][i]

#   for i in range(1, N + 1):
#     for j in range(1, N + 1):
#       if i < j:
#         dp[i][j] = dp[i][j - 1] + P[j]

#         if e < dp[i][j]:
#           e = dp[i][j]

#   print(e)



#  카데인 알고리즘
while True:
  N = int(input())

  if N == 0:
    break

  P = [ int(input()) for _ in range(N) ]

  dp = [ 0 for _ in range(N) ] 

  dp[0] = P[0]

  for i in range(1, N):
    dp[i] = max(P[i], dp[i - 1] + P[i])

  print(max(dp))

