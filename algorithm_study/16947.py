import sys
from collections import deque

input = sys.stdin.readline

def dfs (start, idx, cnt):
  global cycle

  if start == idx and cnt >= 2: # 사이클 종료 조건
    cycle = True
  
  visited[idx] = True # 현재역 방문 표시
  
  for i in adj_list[idx]:
    if not visited[i]: # 다음 역이 방문하지 않은 역인 경우
      dfs( start, i, n + 1 )

    elif i == start and cnt >= 2: # 이미 방문했고, 경로상 2군데의 역을 지난 경우
      dfs( start, i, cnt )


def distance_station():
  global check

  q = deque()

  for i in range(K):
    if cycle[i]:
      check[i] = 0
      q.append(i)

  while q:
    now = q.popleft()

    for i in adj_list[now]:
      if check[i] == -1:
        q.append(i)

        check[i] = check[now] + 1


# 사이클 구하는 문제
K = int(input())

adj = [ map(int, input().split()) for _ in range(K) ]

adj_list = [ [] for _ in range(K + 1) ]

for a in adj:
  i, j = a

  adj_list[i].append(j)
  adj_list[j].append(i)


cycle = [ False ] * ( K )

check = [ -1 ] * ( K )

for i in range(K):

  visied = [False] * n

  is_cycle = False

  dfs(i, i, 0);

  if is_cycle: # 순환역이라면 순환역 표시
    cycle[i] = True

distance_station()

print(*check)