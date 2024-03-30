import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input()) # 노드의 수

M = int(input()) # 간선의 수

edges = [ map(int, input().split()) for _ in range(M)]

adj_list = [ [] for _ in range( N + 1 ) ]
flag = [ False ] * N

for e in edges:
  f, t = e
  adj_list[f].append(t)
  adj_list[t].append(f)

virus_cumputer = 0

def dfs(n):
  flag[n - 1] = True

  for w in adj_list[n]:
    if not flag[w - 1]: 
      dfs(w)

dfs(1)

print(sum(flag) - 1)
