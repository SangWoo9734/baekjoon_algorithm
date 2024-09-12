import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

S = int(input())

graph = [ [] for _ in range(V + 1) ]

for _ in range(E):
  u, v, w = map(int, input().split())

  graph[u].append([v, w])

INF = int(1e9)

value = [ INF for _ in range(V + 1) ]

def dijkstra(start):

  q = []
  heapq.heappush(q, [0, start])
  value[start] = 0

  # print(q)
  
  while q:
    w, v = heapq.heappop(q)

    if w > value[v]:
      continue    
    
    for r in graph[v]:
      cost = w + r[1]

      if cost < value[r[0]]:
        value[r[0]] = cost
        heapq.heappush(q, [cost, r[0]])

dijkstra(S)

for v in value[1:]:
  if v == INF:
    print('INF')
  else:
    print(v)