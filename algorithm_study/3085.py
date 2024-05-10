import sys

input = sys.stdin.readline

N = int(input())

board = [ list(input().rstrip()) for _ in range(N) ]

print(board)

count_board = [ [ [0, 0] for _ in range(N) ] for _ in range(N) ]

count_board[0][0] = [1, 1]

def set_board_count(count_board, i, j):
  print(f'i: {i}, j: {j}')
  if i > 0 and board[i][j] == board[i-1][j]:
    count_board[i][j][0] = count_board[i-1][j][0] + 1
  else:
    count_board[i][j][0] = count_board[i-1][j][0]

  if j > 0 and board[i][j] == board[i][j-1]:
    count_board[i][j][1] = count_board[i][j-1][1] + 1
  else:
    count_board[i][j][1] = count_board[i][j-1][1] 
    
  
  return count_board


def get_max_count(board):

  max_count = 0
  for i in range(N):
    for j in range(N):
      count_board = set_board_count(count_board, i, j)
      if max_count < count_board[i][j]:
        max_count = count_board[i][j]

  return max_count

m_count = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# setting initial count board
for i in range(N):
  for j in range(N):
    count_board = set_board_count(count_board, i, j)

    print(*count_board, sep='\n')

# for i in range(N):
#   for j in range(N):
#     for k in range(4):
#       ni = i + dx[k]
#       nj = j + dy[k]

#       if ( 0 > ni or ni <= N or 0 > nj <= N ):
#         continue

#       board[i][j], board[ni][nj] = board[ni][nj], board[i][j]

#       a = get_max_count(board)
#       if a > m_count:
#         m_count = a

#       board[i][j], board[ni][nj] = board[ni][nj], board[i][j]




print(count_board)


