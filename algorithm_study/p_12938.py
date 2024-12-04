# import sys
# from collections import deque
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#   N = int(input())

#   edges = list(map(int, input().split()))

#   def bfs(n):
#     visited = set()

#     q = deque([n])
#     team = []

#     while q:
#       node = q.popleft()

#       if node in visited:
#         if node in team:
#           return team[team.index(node):]
#         return []
    
#       visited.add(node)
#       team.append(node)
#       q.append(edges[node - 1])

#     return []

#   team_accept = [ False for _ in range(N + 1) ]

#   for i in range(1, N + 1):
#     if not team_accept[i]:
#         team = bfs(i)

#         for t in team:
#           team_accept[t] = True
    
#   print(len(edges) - sum(team_accept))

import sys
from collections import deque

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(node):
  global count

  visited[node] = True

  cycle.append(node)

  next_node = edges[node]

  if not visited[next_node]:
    dfs(next_node)
  elif not finished[next_node]:
    count += len(cycle[cycle.index(next_node):])


  finished[node] = True



T = int(input())

for _ in range(T):
  N = int(input())

  edges = [0] + list(map(int, input().split()))

  visited = [False] * (N + 1)
  finished = [False] * (N + 1)
  count = 0

  for i in range(1, N + 1):
    if not visited[i]:
      cycle = []
      dfs(i)

  

  print(len(edges) - count - 1)