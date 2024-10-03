import sys

input = sys.stdin.readline

# N = int(input())

# nums = list(map(int, input().split()))

# def LCS(X, Y, i, j, dp):
#   if not dp[i][j]:
#     if i == 0 or j == 0:
#       return 0;
#     elif X[i - 1] != Y[j - 1]:
#       dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
#     else:
#       dp[i][j] = dp[i - 1][j - 1] + 1
  
#   return dp[i][j]


# res = N

# for i in range(N):
#   l_target = nums[:i]
#   r_target = nums[i + 1:]

#   if len(l_target) == 0 or len(r_target) == 0:
#     res = min(res, N - 1)
  
#   else:
#     l_str = ''.join(map(str, l_target))
#     r_str = ''.join(map(str, r_target))

#     dp = [ [ 0 for _ in range(len(r_str) + 1) ] for _ in range(len(l_str) + 1) ]

#     for j in range(1, len(l_str) + 1):
#       for k in range(1, len(r_str) + 1):
#         LCS(l_str, r_str, j, k, dp)
    
#     # print(*dp)
#     same = dp[len(l_str)][len(r_str)]

#     res = min(res, N - 1 - same * 2)

# print(res)

# 

n = int(input())
seq = list(map(int, input().split()))

dp = [ [0] * (n + 1) for i in range(n + 1) ]
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if seq[-i] == seq[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    
    print(*dp, sep='\n')
    print()

print(n - dp[n][n])
