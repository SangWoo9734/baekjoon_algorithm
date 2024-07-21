import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [ list(map(int, input().split())) for _ in range(n) ]
visited = [ [False for _ in range(m)] for _ in range(n) ]


dx = [ 1, 0, -1, 0]
dy = [ 0, -1, 0, 1]


def bfs(x, y):
  queue = deque([[x, y]])
  size = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and board[ny][nx] == 1:
        queue.append([nx, ny])
        visited[ny][nx] = True
        size += 1

  return size

count = 0
max_size = 0;

for i in range(n): # 세로
  for j in range(m): # 가로
    if visited[i][j] == False:
      visited[i][j] = True
      if board[i][j] == 1:
        cur_size =  bfs(j, i) 
        count += 1
        max_size = max_size if max_size > cur_size else cur_size;


print(count)
print(max_size)


