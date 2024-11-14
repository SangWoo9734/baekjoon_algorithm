import heapq
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

res = [ 0 for _ in range(N) ]
stack = []

for i, h in list(enumerate(nums))[::-1]:
  if len(stack) == 0:
    res[i] = -1

  else :
    while stack and stack[-1][1] <= h:
      stack.pop()
    
      
    res[i] = stack[-1][1] if stack else -1

  stack.append([i, h])

  # print(stack)

print(*res, sep=' ')
