import sys
from collections import deque

input = sys.stdin.readline

dx = [ 2, 2, 1, -1, -2, -2, -1, 1 ]
dy = [ 1, -1, -2, -2, -1, 1, 2, 2 ]

def bfs(x, y, tx, ty, count):

  visited = [ [ False for _ in range(N) ] for _ in range(N) ]

  queue = deque()
  queue.append([x, y, count])
  visited[y][x] = True
  
  while (queue):
    px, py, c = queue.popleft()

    if px == tx and py == ty:
      print(c)
      return True

    for i in range(8):
      nx = dx[i] + px
      ny = dy[i] + py

      if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
        queue.append([ nx, ny, c + 1 ])
        visited[ny][nx] = True

    # print(*visited, sep="\n")
  return False

K = int(input())

for _ in range(K):
  N = int(input())

  x, y = map(int, input().split())
  tx, ty = map(int, input().split())

  bfs(x, y, tx, ty, 0)
