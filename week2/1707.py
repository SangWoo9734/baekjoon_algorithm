import sys

input = sys.stdin.readline

def dfs ( flag, n, graph, group ):
  flag[n] = group

  for e in graph[n]:
    if flag[e] == 0:
      res = dfs(flag, e, graph, -group)

      if res == False:
        return False
    elif flag[e] == group:
      return False

  return True



K = int(input())

for _ in range(K):
  V, E = map(int, input().split())

  flag = [ 0 ] * ( V + 1 )
  graph = [[] for _ in range( V + 1 )]

  for _ in range(E):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

  for index in range(1, V + 1):
    if flag[index] == 0:
      res = dfs(flag, index, graph, 1)

      if res == False: break
      
  if res== False:
    print("NO")
  else:
    print('YES')