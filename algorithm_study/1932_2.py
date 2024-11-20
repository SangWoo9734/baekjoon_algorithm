import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
triangle = [ list(map(int, input().split())) for _ in range (N)]
res = [ [ 0 for _ in range(i + 1) ] for i in range(N) ]

res[0][0] = triangle[0][0]

q = deque([[0,0]])

for i in range(1, N):
  for j in range(len(triangle[i])):

    left = 0
    right = 0
    
    if j != 0:
      left = res[i-1][j-1] + triangle[i][j]
    if j != len(res[i - 1]):
      right = res[i-1][j] + triangle[i][j]

    res[i][j] = max(res[i][j], left, right)
  
  

print(max(res[-1]))