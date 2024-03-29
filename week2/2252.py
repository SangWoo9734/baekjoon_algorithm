import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input()[:-1].split())

edge_dict = [ [] for _ in range(N + 1)]
edge_count = [ 0 for _ in range(N + 1)]

discovered = []
queue = deque()

for _ in range(M):
  f, t = map(int, input()[:-1].split(' '))
  edge_dict[f].append(t)
  edge_count[t] += 1



for i in range(1, N + 1):
  if edge_count[i] == 0 :
    queue.append(i)

while queue:
  # 큐에서 하나를 뺀다.
  v = queue.popleft()
  discovered.append(v)

  # 해당 노드와 연결된 노드 사이의 간선을 제거한다.
  for w in edge_dict[v]:
    edge_count[w] -= 1
    # 진입차수가 0인 노드를 넣어준다.
    if edge_count[w] == 0:
      queue.append(w)

  # print(f'discovered: {discovered}, queue: {queue}')
  # print(edge_count)
  # print(edge_dict)

# print(' '.join(map(str, discovered)))
print(*discovered)