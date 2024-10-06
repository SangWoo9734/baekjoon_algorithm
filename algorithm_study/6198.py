import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

res = [ 0 for _ in range(N) ]

buildings = deque([ int(input()) for _ in range(N) ])

stack = []

for i, h in list(enumerate(buildings))[::-1]:
  if len(stack) == 0:
    stack.append((i, h))
  else:
    smaller_building = 0
    while stack[-1][1] < h:
      pre_i, _ = stack.pop()
      smaller_building += 1 + res[pre_i]
      if len(stack) == 0:
        break
    
    res[i] = smaller_building
    stack.append((i, h))

print(sum(res))

