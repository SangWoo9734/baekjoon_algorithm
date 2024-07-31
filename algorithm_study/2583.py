import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


M, N, K = map(int, input().split())

area = [ list(map(int, input().split())) for _ in range(K) ]

board = [ [ 0 for _ in range(N) ] for _ in range(M) ]

for y in range(M):
  for x in range(N):
    for a in area:
      x1, y1, x2, y2 = a

      if x1 < x + 1 <= x2 and y1 < y + 1 <= y2:
        board[y][x] = 1


def dfs(x, y, count):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < M and board[ny][nx] == 0:
      board[ny][nx] = 1
      count = dfs(nx, ny, count + 1)

  return count

res = []

for y in range(M):
  for x in range(N):
    if board[y][x] == 0:
      board[y][x] = 1
      res.append(dfs(x, y, 1))
  

print(len(res))
print(' '.join(map(str, sorted(res))))


