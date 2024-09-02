import sys

N = int(input())

route = input().rstrip()

board = [ [ '.' for _ in range(N) ] for _ in range(N) ]


cur = [0, 0]

def move_vertical(x, y):
  
  if board[y][x] == '.':
      board[y][x] = '|'
  elif board[y][x] == '-':
    board[y][x] = '+'
  else:
    return

def move_horiziontal(x, y):
  if board[y][x] == '.':
      board[y][x] = '-'
  elif board[y][x] == '|':
    board[y][x] = '+'
  else:
    return

def move_cursor(x, y, command):
  if command == 'U':
    nx, ny = [x, y - 1]
  elif command == 'D':
    nx, ny = [x, y + 1]
  elif command == 'L':
    nx, ny = [x - 1, y]
  else:
    nx, ny = [x + 1, y]

  if 0 <= nx < N and 0 <= ny < N :
    return [nx, ny]
  else:
    return [x, y]

for r in route:
  x, y = cur

  if r == 'U' and 0 <= y - 1 < N:
    move_vertical(x, y)
    move_vertical(x, y - 1)

    cur = move_cursor(x, y, r)
  elif r == 'D' and 0 <= y + 1 < N:
    move_vertical(x, y)
    move_vertical(x, y + 1)
    cur = move_cursor(x, y, r)

  elif r == 'L' and 0 <= x - 1 < N:
    move_horiziontal(x, y)
    move_horiziontal(x - 1, y)
    cur = move_cursor(x, y, r)

  elif r == 'R' and 0 <= x + 1 < N:
    move_horiziontal(x, y)
    move_horiziontal(x + 1, y)
    cur = move_cursor(x, y, r)

  else:
    continue


  # print(cur)


for row in board:
  print(''.join(row))
