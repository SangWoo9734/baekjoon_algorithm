import sys
from collections import deque
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

# dfs 두번?

N = int(input())

board = [ list(map(int, input().split())) for _ in range(N) ]

visited = [ [ False ]  * N for _ in range(N) ] 

dx = [ 1, 0, -1, 0 ]
dy = [ 0, -1, 0, 1 ]

def labeling_dfs(x, y, visited, i_count):
  board[y][x] = i_count

  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and board[ny][nx] == 1: 
      visited[ny][nx] = True
      labeling_dfs(nx, ny, visited, i_count)

def dist_bfs(i_idx):
  dist_b  = [ [-1] * N for _ in range(N) ]
  q = deque()

  for i in range(N):
    for j in range(N):
      if board[i][j] == i_idx:
        dist_b[i][j] = 0
        q.append([i, j])


  while(q):
    y, x = q.popleft()

    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y

      if 0 <= nx < N and 0 <= ny < N:
        if board[ny][nx] and board[ny][nx] != i_idx:
          return dist_b[y][x] 
        elif board[ny][nx] == 0 and dist_b[ny][nx] == -1:
          dist_b[ny][nx] = dist_b[y][x] + 1
          q.append([ny, nx])
  
  return sys.maxsize

res = sys.maxsize
i_count = 1

#labeling
for i in range(N):
  for j in range(N):
    if not visited[i][j] and board[i][j] == 1:
      visited[i][j] = True
      labeling_dfs(j, i, visited, i_count)

      i_count += 1


# find land
for k in range(1, i_count + 1):
  res = min(dist_bfs(k), res)

print( res )