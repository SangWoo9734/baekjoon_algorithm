import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dist = [ 0 ] * 100001
visited = [ 0 ] * 100001

def show_route(position):
  route = []
  i = position

  for _ in range(dist[position]+1):
    route.append(i)
    i = visited[i]

  print(dist[position])
  print(' '.join(map(str, route[::-1])))


def bfs() :
  q = deque([N])

  while q:
    posit = q.popleft()

    if posit == K:
      show_route(posit)
      return
    

    for p in [ posit + 1, posit - 1, posit * 2 ]:
      if 0 <= p <= 100000 and dist[p] == 0:
        q.append(p)
        dist[p] = dist[posit] + 1
        visited[p] = posit

bfs()