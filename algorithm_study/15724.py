import sys

input = sys.stdin.readline

N, M = map(int, input().split())

ground = [  [0] + list(map(int, input().split())) for _ in range(N) ]

for i in range(N):
  for j in range(1, M + 1):
    ground[i][j] = ground[i][j] + ground[i][j - 1]

K = int(input())

squares = [ list(map(int, input().split())) for _ in range(K) ]

for s in squares:
  x1, y1, x2, y2 = s
  res = 0
  for x in range(x1 - 1, x2):
    res += ground[x][y2] - ground[x][y1 - 1]
  
  print(res)
