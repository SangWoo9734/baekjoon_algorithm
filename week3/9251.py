import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

X, Y = [ input()[:-1] for _ in range(2) ]

dp = [ [ 0 ] * ( len(Y) + 1 ) for _ in range( len(X) + 1 ) ]

def LCS(i, j):
  if not dp[i][j]:
    # print(f'X[i]: {i}, Y[j]: {j}')
    if i == 0 or j == 0:
      return 0
    elif X[i - 1] != Y[j - 1]:
      # Bottom-UP
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      # Top-Down
      # dp[i][j] = max(LCS(i - 1, j), LCS(i, j - 1))
    else: # X[i] = Y[j] 
      # Bottom-UP
      dp[i][j] = dp[i-1][j-1]+ 1

      # Top-Down
      # dp[i][j] = LCS(i - 1, j - 1) + 1
  return dp[i][j]

# Bottom-UP
for i in range(1, len(X) + 1):
  for j in range(1, len(Y) + 1):
    LCS(i, j)

#Top-Down
# LCS(len(X), len(Y))

print(dp[len(X)][len(Y)])