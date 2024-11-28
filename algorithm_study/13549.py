import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

max_limit = 100001
timer = [ -1 ] * max_limit

q = deque([N])
timer[N] = 0

while q:
  cur = q.popleft()


  if cur == K:
    print(timer[cur])
    break

  for next_pos, cost in [(cur * 2, 0), (cur + 1, 1), (cur - 1, 1)]:
    if 0 <= next_pos < max_limit and (timer[next_pos] == -1 or timer[next_pos] > timer[cur] + cost):
      timer[next_pos] = timer[cur] + cost

      if cost == 0:
        q.appendleft(next_pos)

      else:
        q.append(next_pos)