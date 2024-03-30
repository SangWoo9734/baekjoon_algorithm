import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

adj_list = [ [] for _ in range(N + 1) ]
# flag = [ False ] * (N + 1)
p_node = [ 0 ] * (N + 1)

for _ in range(N - 1):
  f, t = map(int, input().split())
  adj_list[f].append(t)
  adj_list[t].append(f)

stack = [1]

while stack:
  cur = stack.pop()
  
  for i in  adj_list[cur]:
    if p_node[i] == 0:
      p_node[i] = cur
      stack.append(i)

# def dfs(n):
#   flag[n] = True

#   for w in adj_list[n]:
#     if not flag[w]:
#       p_node[w - 2] = n
#       dfs(w)

# dfs(1)

print(*p_node[2:], sep='\n')
