import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, board):

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1:
      board[ny][nx] = 0
      board = dfs(nx, ny, board)

  return board

T = int(input())

for _ in range(T):
  M, N, K = map(int, input().split())

  ground = [ [ 0 for _ in range(M) ] for _ in range(N) ]

  for _ in range(K):
    x, y = map(int, input().split())
    ground[y][x] = 1

  count = 0
  for y in range(N):
    for x in range(M):
      if ground[y][x] == 1:
        ground[y][x] = 0
        ground = dfs(x, y, ground)
        count += 1

  print(count)