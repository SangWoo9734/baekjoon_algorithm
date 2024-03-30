import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M =  map(int, input().split())

edges = [ map(int, input().split()) for _ in range(M) ]

adj_list = [ [  ] for _ in range (N + 1) ]
flag = [ False ] * (N + 1)

for e in edges:
  f, t = e
  # 인접 행렬
  # adj_list[f - 1][t - 1] = 1
  # adj_list[t - 1][f - 1] = 1

  # 인접 리스트
  adj_list[f].append(t)
  adj_list[t].append(f)

# print(*adj_list, sep='\n')
# print('------------------------------------')

V = 1 # 시작 노드
count = 0

stack = [ V ]

def bfs(n):
  # v = stack.pop()
  flag[n] = True

  for i in adj_list[n]:
    if not flag[i]:
      stack.append(i)
      bfs(i)

for i in range(1, N + 1):
  if not flag[i]:
    bfs(i)
    count += 1
    

print(count)
