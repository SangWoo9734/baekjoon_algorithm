import sys
import copy

sys.setrecursionlimit(10**8)

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())

nboard = [ list(input().rstrip()) for _ in range(N) ]
yboard = [ copy.deepcopy(r) for r in nboard ]

for y in range(N):
  for x in range(N):
    if yboard[y][x] == 'G':
      yboard[y][x] = 'R'

def dfs(x, y, board, target):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == target:
      board[ny][nx] = 'X'
      board = dfs(nx, ny, board, target)

  return board

ncount = 0
ycount = 0

for y in range(N):
  for x in range(N):
    if nboard[y][x] != 'X':
      ncount += 1
      nboard = dfs(x, y, nboard, nboard[y][x])

    if yboard[y][x] != 'X':
      ycount += 1
      yboard = dfs(x, y, yboard, yboard[y][x])

print(f'{ncount} {ycount}')