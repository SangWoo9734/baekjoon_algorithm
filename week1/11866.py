import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split(' ')))

result = []
q = deque()

for i in range(1, N + 1):
  q.append(i)

while len(q) > 0:
  q.rotate((K  - 1) * -1)
  value = q.popleft()
  result.append(value)

joined_result = ', '.join(map(str, result))

print(f'<{joined_result}>')