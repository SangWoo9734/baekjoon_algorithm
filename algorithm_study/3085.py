import sys
from collections import Counter
from collections import deque
input = sys.stdin.readline

N = int(input())

board = [ list(input().rstrip()) for _ in range(N) ]
visited = [ [ 0 for _ in range(N) ] for _ in range(N) ]

def get_count(arr):
  max_count = 1
  count = 1
  for a in range(1, len(arr)):
    if arr[a] == arr[a - 1]:
      count += 1
    else:
      max_count = max(count, max_count)
      count = 1

  max_count = max(count, max_count)
  
  return max_count

m_count = 0

dx = [1, 0]
dy = [0, 1]

for i in range(N):
  m_count = max(m_count, get_count([ board[i][j] for j in range(N) ]), get_count([ board[j][i] for j in range(N) ]))

q = deque([[0, 0]])
visited[0][0] = 0

for y in range(N):
  for x in range(N):
    for i in range(2):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < N:

        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

        if nx == x:
          m_count = max(get_count([board[ny][i] for i in range(N)]), get_count([board[y][i] for i in range(N)]), get_count([board[i][x] for i in range(N)]), m_count)
        else:
          m_count = max(get_count([board[i][nx] for i in range(N)]), get_count([board[i][x] for i in range(N)]), get_count([board[y][i] for i in range(N)]), m_count)

        board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(m_count)