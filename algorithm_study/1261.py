import sys
# from collections import deque
import heapq

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

M, N = map(int, input().split())

room = [ list(map(int, list(input().rstrip()))) for _ in range(N) ]

visited = [ [ False for _ in range(M) ] for _ in range(N) ]

q = [[0, 0, 0]]
visited[0][0] = True

while q:
  cost, x, y = heapq.heappop(q)

  if x == M - 1 and y == N - 1:
    print(cost)
    break

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == False:
      visited[ny][nx] = True
      
      if room[ny][nx] == 0:
        heapq.heappush(q, [cost, nx, ny])
      else:
        heapq.heappush(q, [cost + 1, nx, ny])
  
  print(q)
