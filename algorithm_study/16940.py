import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [ set() for _ in range(N + 1) ]

for _ in range(N - 1):
  a, b = map(int , input().split())

  graph[a].add(b)
  graph[b].add(a)

target = list(map(int, input().split()))


i = 1

q = deque([1])

ans = 1

while i < N:

  q.append(target[i])

  while len(graph[q[0]]) == 0:
    q.popleft()
  
  if target[i] not in graph[q[0]]:
    ans = 0

    break
  

  graph[q[0]] -= set([target[i]])
  graph[target[i]] -= set([q[0]])

  i += 1

print(ans)