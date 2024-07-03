import sys

input = sys.stdin.readline

N, M = map(int, input().split())

army = [ list(input()) for _ in range(M) ]

visited = [ [ False for _ in range(N) ] for _ in range(M) ]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs (x, y, visited, type, count):
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<= nx < N and 0 <= ny < M and visited[ny][nx] == False and type == army[ny][nx]:
      visited[ny][nx] = True
      count += 1
      count = dfs(nx, ny, visited, type, count)

  return count

W = 0
B = 0

for i in range(M):
  for j in range(N):
    if visited[i][j] == False:
      visited[i][j] = True
      size = dfs(j, i, visited, army[i][j], 1)

      if army[i][j] == "W":
        W += size ** 2
      else:
        B += size ** 2


print(f"{W} {B}")
