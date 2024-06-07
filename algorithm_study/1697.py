import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

visited = [ False ] * 100001

q = deque()

q.append([N, 0])
visited[N] = True

while q:
  p, t = q.popleft()

  if p == K:
    print(t)
    break


  if p - 1 >= 0 and not visited[p - 1]:
    visited[p - 1] = True
    q.append([p - 1, t + 1])
  
  if p + 1 <= 100000 and not visited[p + 1]:
    visited[p + 1] = True

    q.append([p + 1, t + 1])

  if p <= 50000 and not visited[p * 2]:
    visited[p * 2] = True

    q.append([p * 2, t + 1])