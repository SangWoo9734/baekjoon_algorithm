import sys

input = sys.stdin.readline

def check_is_circle (x, y, board, visited):
  c  = 0
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    if 0 <= nx < M and 0 <= ny < N and visited[y][x] == visited[ny][nx] == True and board[y][x] == board[ny][nx]:
      c += 1
    
  return True if c > 1 else False

def dfs ( x, y, board, visited ):
  if check_is_circle( x, y, board, visited ):
    return True

  res = False

  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y

    if 0 <= nx < M and 0 <= ny < N:
      if board[ny][nx] == board[y][x]:
        if visited[ny][nx] == False:
          visited[ny][nx] = True
          res = True if res else dfs(nx, ny, board, visited)


  return res 


N, M = map(int, input().split())

board = [ input().rstrip() for _ in range(N) ]

visited = [ [ False ] * M for _ in range (N)]

dx = [ 1, 0, -1, 0 ]
dy = [ 0, -1, 0, 1 ]

res = False

for i in range(N):
  for j in range(M):
    # print(f'j: {j}, i: {i}')
    if visited[i][j] == False :
      visited[i][j] = True
      res = True if res else dfs(j, i, board, visited)

print("Yes" if res else "No")