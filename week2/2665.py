import sys
import heapq

input = sys.stdin.readline

N = int(input())

maze = [ list(map(int, input()[:-1])) for _ in range(N) ]
visited = [ [ False ] * N for _ in range(N) ]

queue = [[0, 0, 0]]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

while queue:
  cost, x, y = heapq.heappop(queue)
  if x == N - 1 and y == N - 1:
    print(cost)
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == False:
      visited[ny][nx] = True
      if maze[ny][nx] == 1:
        heapq.heappush(queue, [cost, nx, ny])
      else:
        heapq.heappush(queue, [cost + 1, nx, ny])