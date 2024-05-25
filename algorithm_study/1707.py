import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

def dfs(n, color, ad_list):
  for m in ad_list[n]:
    if color[m] == 0:
      color[m] = 1 if color[n] == 2 else 2
      res = dfs(m, color, ad_list)
      if res == False:
        return False
    elif color[m] == color[n]:
      return False

  return True

K = int( input() )

for _ in range(K):
  is_all_visit = False

  V, E = map(int, input().split())

  adj = [ list(map(int, input().split())) for _ in range(E) ]

  ad_list = [ [] for _ in range(V + 1) ] 

  for a in range(E):
    # print(adj[a])
    i, j = adj[a]
    ad_list[i].append(j)
    ad_list[j].append(i)
  
  color = [ 0 ] * ( V + 1 ) 

  for v in range(1, V + 1):
    if color[v] == 0:
      color[v] = 1
      res = dfs(v, color, ad_list)

      if res == False: break
  
  print('YES' if res else 'NO' )
  
