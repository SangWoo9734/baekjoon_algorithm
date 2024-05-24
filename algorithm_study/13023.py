import sys
import heapq

input = sys.stdin.readline

N, M = map( int, input().split() )

relations = [ map(int, input().split()) for _ in range(M) ]

rel_list = [ [] for _ in range(N) ]

for r in relations:
  a, b = r

  rel_list[a].append(b)
  rel_list[b].append(a)



def dfs (v, count, vistied, res):
  # print(v)
  if count == 4:
    return 1


  for w in rel_list[v]:
    if not visited[w]:
      visited[w] = True
      res = dfs(w, count + 1, visited, res)
      visited[w] = False

  return res


for i in range(N):
  visited = [ False ] * N
  visited[i] = True
  f = dfs(i, 0, visited, 0)

  if f == 1:
    break

print(f)


# queue = [ 0 ]
# is_friend = [ False ] * N

# while queue:
#   p = heapq.heappop(queue)

#   is_friend[p] = True

#   for i in rel_list[p]:
#     if is_friend[i] == False:
#       heapq.heappush(queue, i)

# print(is_friend)

# print(int( N == sum(is_friend) ))