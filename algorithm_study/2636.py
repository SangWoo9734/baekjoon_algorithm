import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r, c = map(int, input().split())
board = []
total_cheese = 0

for _ in range(r):
  row = list(map(int, input().split()))
  board.append(row)

  total_cheese += sum(row)

def bfs():
  visited = [ [ False for _ in range(c) ] for _ in range(r) ]
  visited[0][0] = True

  q = deque([[0, 0]])
  melt = set([])

  while q:
    x, y = deque.popleft(q)

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < c and 0 <= ny < r and visited[ny][nx] == False:
        if board[ny][nx] == 1:
            melt.add((nx, ny))
        else:
          visited[ny][nx] = True
          deque.append(q, [nx, ny])

      
  for m in melt:
    x, y = m
    board[y][x] = 0

  return len(melt)

time = 1

while True:
  cur_melt_cheeses = bfs()
  total_cheese -= cur_melt_cheeses

  if total_cheese == 0:
    print(time)
    print(cur_melt_cheeses)
    break

  time += 1