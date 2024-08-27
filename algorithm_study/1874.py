import sys

input = sys.stdin.readline

N = int(input())

target = [ int(input()) for _ in range(N) ]

stack = []

res = []
target_index = 0

for i in range(1, N + 1):

  stack.append(i)
  res.append('+')

  while stack[-1] == target[target_index]:
    stack.pop();
    res.append('-')
    target_index += 1

    if not stack:
      break
  
  
  # print(f'stack : {stack}')
  # print(f'res : {res}')

  # print('')

if len(stack) > 0:
  print("NO")
else:
  print(*res, sep='\n')