import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [ [] for _ in range(N + 1) ]
distance = [ sys.maxsize ] * (N + 1)

for _ in range(M):
  f, t, c = map(int, input().split())

  graph[f].append([t, c])

start, end = map(int, input().split())

q = [[start, 0]]
distance[start] = 0
visited = [ False ] * ( N + 1 )


while q:
  cur, dist = heapq.heappop(q)

  print(cur, dist)

  print(f'before: cur: {cur}, dist:{dist}')
  if distance[cur] < dist:

    print(f'after: cur: {cur}, dist:{dist}')
    continue

  for e in graph[cur]:
    node, value = e

    if dist + value < distance[node]:
      distance[node] = dist + value
      print([node, distance[node]])
      heapq.heappush(q, [node, distance[node]])

  # print(distance)

print(distance[end])
