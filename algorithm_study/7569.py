import sys
from collections import deque

input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

tomatos = [ ] 

for h in range(H):
  floor = []
  for n in range(N):
    floor.append(list(map(int, input().split())))
  tomatos.append(floor)

q = deque()
for z in range(H):
  for y in range(N):
    for x in range(M):
      if tomatos[z][y][x] == 1:
        q.append([x, y, z])

while q:
  x, y, z = q.popleft()

  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]

    if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatos[nz][ny][nx] == 0:
      tomatos[nz][ny][nx] = tomatos[z][y][x] + 1
      q.append([nx, ny, nz])

res = 0
for z in range(H):
  for y in range(N):
    for x in range(M):
      if tomatos[z][y][x] == 0:
        print(-1)
        exit(0)
      
      res = max(res, tomatos[z][y][x])

print(res - 1)