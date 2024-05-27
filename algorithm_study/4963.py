import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs (m, n, x, y, board):

  for i in range(8):
    nx = dx[i] + x
    ny = dy[i] + y

    if (-1 < nx < m) and (-1 < ny < n) and board[ny][nx]:
      board[ny][nx] = 0
      board = dfs(m, n, nx, ny, board)

  return board



dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, -1, 0, 1, 1, -1, 1, -1]


while (1) :
  m, n = map(int, input().split())

  if (m + n == 0) : break

  board = [ list(map(int, input().split())) for _ in range(n) ]
  count = 0

  for i in range(n):
    for j in range(m):
      if board[i][j]:
        board = dfs(m, n, j, i, board)
        count += 1

  print(count)
