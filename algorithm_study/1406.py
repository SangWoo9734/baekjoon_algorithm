import sys
from collections import deque

input = sys.stdin.readline

target = input().rstrip()

N = int(input())

commands = [ input().split() for _ in range(N) ]

l_stack = deque(list(target))
r_stack = deque([])

for c in commands:

  if c[0] == "L":
    if l_stack:
      l = l_stack.pop()
      r_stack.append(l)

  elif c[0] == "D":
    if r_stack:
      l = r_stack.pop()
      l_stack.append(l)
  
  elif c[0] == "B":
    if l_stack:
      l_stack.pop()
  
  else :
    l_stack.append(c[1])

result = ''

r_stack.reverse()
print(''.join(l_stack + r_stack))