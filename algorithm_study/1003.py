import sys

input = sys.stdin.readline

T = int(input())

case = [ int(input()) for _ in range(T) ]

max_case = max(case)

dp = [ [0, 0] for _ in range(max_case + 1) ]

for i in range(max_case + 1):
  if i == 0:
    dp[i] = [1, 0]
  elif i == 1:
    dp[i] = [0, 1]
  else :
    x1, y1 = dp[i - 2]
    x2, y2 = dp[i - 1]
    dp[i] = [x1 + x2, y1 + y2]

# print(*dp, sep="\n")

for c in case:
  res = dp[c]
  print(f'{res[0]} {res[1]}')