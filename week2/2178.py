import sys
import copy
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

maze = [ list(map(int, input()[:-1])) for _ in range(N) ]
distance = [ [ 0 ] * M for _ in range(N) ]
distance[0][0] = 1

# print(*maze, sep="\n")

q = deque([[0, 0]])

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while q:
  x, y = q.popleft()

  for d in zip(dx, dy):
    nx = x + d[0]
    ny = y + d[1]
    # print(f'x: {x}, y: {y}, nx: {nx}, ny: {ny}')
    if  nx < 0 or nx >= M or ny < 0 or ny >= N:
      continue

    if maze[ny][nx] != 0 and distance[ny][nx] == 0:
      q.append([nx, ny])
      distance[ny][nx] = distance[y][x] + 1
  

print(distance[N-1][M-1])