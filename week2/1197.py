import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

edges = [ list(map(int, input().split())) for _ in range(E) ]
parent = [ x for x in range( V + 1 ) ]
flag = [ False for _ in range( V + 1 ) ]
wtf = []

# adjedctive list
adj_list = [ [] for _ in range( V + 1 )]
for e in edges:
  a, b, c = e
  adj_list[a].append([b, c])
  adj_list[b].append([a, c])


# Kruscal Algorithm
sorted_edges = sorted(edges, key = lambda x : x[-1])
cost = 0

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

for e in sorted_edges:
  A, B, C = e

  p_a = find_parent(parent, A)
  p_b = find_parent(parent, B)

  if p_a == p_b:
    continue

  else:
    if p_a < p_b:
      parent[p_a] = p_b
    else:
      parent[p_b] = p_a

  cost += C

print(cost)




# prim algorithm
# q = [(0, 1, 1)]
# total_cost = 0

# while q:
#   cost, node, prev = heapq.heappop(q)

#   if flag[node] is True:
#     continue
  
#   wtf.append([cost, node, prev])
#   flag[node] = True
#   # g[node][prev] = 1
#   # g[prev][node] = 1
#   total_cost += cost
  

#   for dst, weight in adj_list[node]:
#     if flag[dst] is False:
#       heapq.heappush(q, (weight, dst, node))

#   # print(q)

# print(total_cost)