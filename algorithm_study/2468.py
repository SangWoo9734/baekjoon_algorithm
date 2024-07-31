import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

N = int(input())

board = [ list(map(int, input().split())) for _ in range(N) ]

_min = sys.maxsize
_max = 0

for y in range(N):
  for x in range(N):
    if _max < board[y][x]:
      _max = board[y][x]
    if _min > board[y][x]:
      _min = board[y][x]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, island):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < N and 0 <= ny < N and island[ny][nx] == 0:
      island[ny][nx] = 1
      island = dfs(nx, ny, island)

  return island



max_island_count = 1
for i in range(_min, _max + 1):
  island = [ [0 for _ in range(N)] for _ in range(N) ]

  for y in range(N):
    for x in range(N):
      if board[y][x] <= i:
        island[y][x] = 1
  
  island_count = 0
  for y in range(N):
    for x in range(N):
      if island[y][x] <= 0:
        island_count += 1
        island = dfs(x, y, island)

  max_island_count = max(max_island_count, island_count)

print(max_island_count)