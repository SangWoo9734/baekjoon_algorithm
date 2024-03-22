import sys

number_of_boards = int(sys.stdin.readline())

call_queue = []

def move(n, x = 1, y = 3):
  if n > 1:
    move(n - 1, x, 6 - x - y)
  
  call_queue.append(f'{x} {y}')

  if n > 1:
    move(n - 1, 6 - x - y, y)


if number_of_boards < 21:
  move(number_of_boards)

  print(len(call_queue))
  for call in call_queue:
    print(call)

else:
  move(20)

  result = len(call_queue)

  for _ in range(number_of_boards - 20):
    result = 2 * result + 1
  
  print(result)
