import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

adj_list = [ [] for _ in range( N + 1 ) ]

for _ in range(M):
  f, t = map(int, input().split())
  adj_list[f].append(t)

distance = [ 0 ] * (N + 1)
queue = deque([ X ])
result = []

while queue:
  cur = queue.popleft()

  for vc in adj_list[cur]:
    if distance[vc] == 0 and vc != X:
      distance[vc] = distance[cur] + 1
      queue.append(vc)
      
      if distance[vc] > K:
        break
      
      if distance[vc] == K:
        result.append(vc)

  print(distance)
if len(result) == 0:
  print(-1)
else:
  print(*sorted(result), sep='\n')