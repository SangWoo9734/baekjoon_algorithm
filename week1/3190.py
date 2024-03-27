import sys
from collections import deque

def snake_move(position, direction):
  move_x, move_y = direction
  match ( move_x, move_y ):
    case ( True, True ):
      return [ position[0] + 1, position[1] ]
    case ( True, False ):
      return [ position[0] - 1, position[1] ]
    case ( False, True ):
      return [ position[0], position[1] - 1]
    case ( False, False ):
      return [ position[0], position[1] + 1]

def move_head_direction(letter, head_direction):
  move_x, move_y = head_direction
  match letter:
    case 'D': # 오른쪽 회전
      if move_x:
        move_x = False
        move_y = not move_y
      else:
        move_x = not move_x
    case 'L':
      if move_x:
        move_x = False
      else :
        move_y = not move_y
        move_x = not move_x

  return [move_x, move_y]
  
N = int(sys.stdin.readline())

A = int(sys.stdin.readline())
apples = [ list(map(int, sys.stdin.readline()[:-1].split(' '))) for _ in range(A) ]

O = int(sys.stdin.readline())
orders = [ list(sys.stdin.readline()[:-1].split(' ')) for _ in range(O) ]

move_x = True
move_y = True

snake_head = [1, 1]
snake_head_lagacy = deque([snake_head])

life_time = 0
order_index = 0

# 사과 위치 설정
apple_matrix = [ [ False ] * N for _ in range(N) ]

for a in apples:
  x, y = a
  apple_matrix[y-1][x-1] = True

while True:
  # 매초 시간이 흐른다.
  life_time += 1
  next_head = snake_move(snake_head, (move_x, move_y))

  # 벽에 머리를 박아 죽는 경우
  if next_head[0] > N:
    break
  if next_head[1] > N:
    break
  elif next_head[0] < 1 or next_head[1] < 1:
    break
  

  # 몸에 머리를 박아 죽는 경우
  elif next_head in snake_head_lagacy:
    break

  # 매초 대가리와 꼬리를 이동한다.
  snake_head = snake_move(snake_head, (move_x, move_y))
  snake_head_lagacy.appendleft(snake_head)


  # 대가리가 사과를 먹으면 몸통 늘어남 (머리만 이동, 꼬리는 가만히)
  if not apple_matrix[snake_head[0] - 1][snake_head[1] - 1]:
    snake_head_lagacy.pop()
  else:
    apple_matrix[snake_head[0] - 1][snake_head[1] - 1] = False


  # 특정 초되면 대가리를 흔든다.
  if order_index < O and orders[order_index][0] == str(life_time):
    _, direction = orders[order_index]
    move_x, move_y = move_head_direction(direction, (move_x, move_y))
    order_index += 1

print(life_time)