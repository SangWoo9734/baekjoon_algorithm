import sys

input = sys.stdin.readline

T = int(input())


def air_dfs( n, count, visited):
  if sum(visited) == N:
    return count


  for i in graph[n]:
    if not visited[i]:
      count += 1
      visited[i] = True
      count = air_dfs(i, count, visited)

  return count


for _ in range(T):
  N, M = map(int, input().split())

  graph_line = [ map(int, input().split()) for _ in range(M) ]

  graph = [ [] for _ in range(N + 1) ]

  for gl in graph_line:
    f, t = gl
    graph[f].append(t)
    graph[t].append(f)

  visited = [ False for _ in range(N + 1) ]
  visited[1] = True


  print(air_dfs(1, 0, visited))

# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#   N, M = map(int, input().split())

#   print(N - 1)

#   graph_line = [ map(int, input().split()) for _ in range(M) ]



