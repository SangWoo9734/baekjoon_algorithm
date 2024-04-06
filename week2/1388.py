import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = [ input()[:-1] for _ in range(N) ]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited = [ [ False ] * M for _ in range(N) ]

total = 0

for n in range(N):
  for m in range(M):
    if visited[n][m] == False:
      if board[n][m] == '-':
        x_index = m + 1
        while 0 <= x_index < M:
          if board[n][x_index] == '-':
            visited[n][x_index] = True
            x_index += 1
            
          
          else:  break
        
        total += 1
      else:
        y_index = n + 1
        while 0<= y_index < N:
          if board[y_index][m] == '|':
            visited[y_index][m] = True
            y_index += 1
            
          
          else:  break
        
        total += 1

print(total)