import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M, k = map(int, input().split())

cost = [ 0 ] + list(map(int, input().split()))

graph = {}

for i in range(N):
  graph[i + 1] = [];

for _ in range(M):
  a, b = map(int, input().split())

  graph[a].append(b);
  graph[b].append(a);

visited = [ False ] * (N + 1)

def dfs (node, res):
  for n in graph[node]:
    if visited[n] == False:
      visited[n] = True
      res.append(n)
      res = dfs(n, res)
  
  return res

linked_node = []

for i in range(1, N + 1):
  if visited[i] == False:
    visited[i] = True
    res = dfs(i, [i])
    linked_node.append(res)

total_cost = 0

for ln in linked_node:
  min_cost = min(list(map(lambda x : cost[x], ln)))
  total_cost += min_cost

if total_cost <= k:
  print(total_cost)
else:
  print('Oh no')
