import sys
from collections import deque

input = sys.stdin.readline

dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

N, M, K = map(int, input().split())

board = [ [ 0 for _ in range(M) ] for _ in range(N) ]

for _ in range(K):
  r, c = map(int, input().split())

  board[r - 1][c - 1] = 1

visited = [ [ False for _ in range(M) ] for _ in range(N) ]

def bfs(x, y):
  q = deque([[x, y]])

  trash_size = 1

  while q:
    x, y = deque.popleft(q)

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False and board[ny][nx] == 1:
        visited[ny][nx] = True
        trash_size += 1
        deque.append(q, [ nx, ny ])

  return trash_size

max_trash_size = 0

for y in range(N):
  for x in range(M):
    if visited[y][x] == False and board[y][x] == 1:
      visited[y][x] = True
      cur_trash_size = bfs(x, y)
      max_trash_size = max(max_trash_size, cur_trash_size)

print(max_trash_size)