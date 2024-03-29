import sys
from collections import deque

input = sys.stdin.readline

#init
N, M, V = map(int, input().rstrip().split(' '))
edges = [ list(map(int, input().rstrip().split(' '))) for _ in range(M)]

adj_list = [ [] for _ in range(N + 1) ]


for e in edges:
  f, t = e

  adj_list[f].append(t)
  adj_list[t].append(f)

adj_list = list(map(sorted, adj_list))

# dfs
def recursive_dfs(v, discovered = []):
  discovered.append(v)

  for w in adj_list[v]:
    if not w in discovered:
      discovered = recursive_dfs(w, discovered)

  return discovered

def loop_dfs(start):
  discovered = [ ]
  stack = [start]
  while stack:
    v = stack.pop()
    if v not in discovered:
      discovered.append(v)
      for w in adj_list[v][::-1]:
        stack.append(w)

  return discovered

#bfs
def bfs(start):
  discovered = [ start ]
  queue = [ start ]

  while queue:
    v = queue.pop(0)
    for w in adj_list[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)

  return discovered


res_dfs = recursive_dfs(V)
print(' '.join(map(str, res_dfs)))

res_bfs = bfs(V)
print(' '.join(map(str, res_bfs)))
