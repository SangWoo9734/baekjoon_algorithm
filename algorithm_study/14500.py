import sys

input = sys.stdin.readline

# 5가지 도형
def shape1(board, x, y):
  if x + 3 >= len(board[0]) or y >= len(board):
    return -1

  return board[y][x] + board[y][x + 1] + board[y][x + 2] + board[y][x + 3] 

def shape2(board, x, y):
  if x + 1 >= len(board[0]) or y + 1 >= len(board):
    return -1

  return board[y][x] + board[y][x + 1] + board[y + 1][x] + board[y + 1][x + 1]

def shape3(board, x, y):
  if x + 1 >=len(board[0]) or y + 2 >= len(board):
    return -1
  
  return board[y][x] + board[y + 1][x] + board[y + 2][x] + board[y + 2][x + 1]

def shape4(board, x, y):
  if x + 1 >= len(board[0]) or y + 2 >= len(board):
    return -1
  
  return board[y][x] + board[y + 1][x] + board[y + 1][x + 1] + board[y + 2][x + 1]


def shape5(board, x, y):
  if x + 2 >= len(board[0]) or y + 1 >= len(board):
    return -1
  
  return board[y][x] + board[y][x + 1] + board[y + 1][x + 1] + board[y][x + 2]

# board rotate
def deg_90 (board):
  new_board = [ [ 0 ] * N  for _ in range(M) ] 

  for n in range(N):
    for m in range(M):
      # print(f'm: {m}, n: {n}')
      new_board[m][n] = board[N - n - 1][m]

  return new_board

def deg_180 (board):
  new_board = [ [ 0 ] * M  for _ in range(N) ] 

  for n in range(N):
    for m in range(M):
      # print(f'm: {m}, n: {n}')
      new_board[n][m] = board[N - n - 1][m]
  return new_board

def deg_270(board):
  new_board = [ [ 0 ] * N  for _ in range(M) ]

  for n in range(N):
    for m in range(M):
      # print(f'm: {m}, n: {n}')
      new_board[m][n] = board[n][M - m - 1]

  return new_board

def oposite(board):
  new_board = [ [ 0 ] * M  for _ in range(N) ]

  for n in range(N):
    for m in range(M):
      # print(f'm: {m}, n: {n}')
      new_board[n][m] = board[n][M - m - 1]

  return new_board

N, M = map(int, input().split());

board = [ list(map(int, input().split())) for i in range(N) ]


res = 0

oposite_board = oposite(board)
boards = [ board, deg_90(board), deg_180(board), deg_270(board), oposite_board, deg_90(oposite_board), deg_180(oposite_board), deg_270(oposite_board)]

for b in boards:
  for i in range(len(b)):
    for j in range(len(b[0])):
      # print(f'x: {j}, y: {i}')
      # print(f'res: {res}, 1: {shape1(board, j, i)}, 2: {shape2(board, j, i)}, 3: {shape3(board, j, i)}, 4: {shape4(board, j, i)}, 5: {shape5(board, j, i)}')
      res = max(res, shape1(b, j, i), shape2(b, j, i), shape3(b, j, i), shape4(b, j, i), shape5(b, j, i))

print(res)

# 모범 답안
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# max_num = max(map(max, board))

# d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
# answer = 0

# def dfs(r, c, cnt, res):
#     global answer
#     if res + (4 - cnt) * max_num < answer:
#         return
    
#     if cnt == 4:
#         answer = max(answer, res)
#         return
    
#     for dr, dc in d:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0:
#             temp = board[nr][nc]
#             if cnt == 2:
#                 board[nr][nc] = 0
#                 dfs(r, c, cnt + 1, res + temp)
#                 board[nr][nc] = temp
            
#             board[nr][nc] = 0
#             dfs(nr, nc, cnt + 1, res + temp)
#             board[nr][nc] = temp
    
# def solution():
#     for i in range(N):
#         for j in range(M):
#             temp = board[i][j]
#             board[i][j] = 0
#             dfs(i, j, 1, temp)
#             board[i][j] = temp
#     return answer

# print(solution())