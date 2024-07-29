import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


M, N = map(int, input().split())

tomatos = [ list(map(int, input().split())) for _ in range(N) ]

queue = deque()

for y in range(N):
  for x in range(M):
    if tomatos[y][x] == 1:
      queue.append([x,y])

while queue:
    x, y = queue.popleft();

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < M and 0 <= ny < N and tomatos[ny][nx] == 0:
        tomatos[ny][nx] = tomatos[y][x] + 1
        queue.append([nx, ny])

res = 0
for y in range(N):
  for x in range(M):
    if tomatos[y][x] == 0:
      print(-1)
      exit(0)

    res = max(res, tomatos[y][x])

print(res - 1)
