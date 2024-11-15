import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
friendship = [ [] for _ in range(N + 1) ]

while True:
  t, f = map(int, input().split())

  if t == -1 and f == -1:
    break;

  friendship[t].append(f)
  friendship[f].append(t)

chairman = [ 0 for _ in range(N + 1) ]

for i in range(1, N + 1):
  visited = [ 0 for _ in range(N + 1) ]
  q = deque([i])

  while q:
    node = deque.popleft(q)
    
    for n in friendship[node]:
      if visited[n] == 0 and n != i:
        visited[n] = visited[node] + 1
        deque.append(q, n)

  chairman[i] = max(visited)

chairman_value = min(chairman[1:])
chairman_list = [ i for i, value in enumerate(chairman) if value == chairman_value]

print(f'{chairman_value} {len(chairman_list)}')
print(*chairman_list)