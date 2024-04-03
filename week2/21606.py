import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
  visited[v] = True
  
  in_count = 0
  for e in graph[v]:
    if  A[e] == 1:
      in_count += 1
    elif not visited[e] and A[e] == 0:
      in_count += dfs(e)

  return in_count

N = int(input())
A = [0] + [ int(i) for i in input()[:-1] ]
graph = [ [] for _ in range(N + 1) ]
visited = [ False ] * ( N + 1 )
total = 0

for _ in range(N - 1):
  f, t = map(int, input().split())
  graph[f].append(t)
  graph[t].append(f)
  if A[f] == 1 and A[t] == 1: # CASE 2
    total += 2

for n in range(1, N + 1):
  if A[n] == 0 and visited[n] == False: # CASE 1
      in_count = dfs(n)
      total += in_count * (in_count - 1)

print(total)


# for _ in range(N - 1):
#   f, t = map(int, input().split())
#   graph[f].append(t)
#   graph[t].append(f)

# count = 0

# def dfs(start):
#   global count

#   for e in graph[start]:
#     if visited[e] == False:
#       visited[e] = True
#       if A[e] == True:
#         count += 1
#       else:
#         dfs(e)

#   return count


# for n in range(1, N + 1):
#   visited = [ False ] * ( N + 1 )
#   if A[n] == 1:
#     visited[n] = True
#     dfs(n)


# print(count)

