import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

visit = [ False for _ in range(F + 1) ]
click = [ 0 for _ in range(F + 1) ]

queue = deque([S])
visit[S] = True

while queue:
  s = queue.popleft()

  
  if s + U <= F and not visit[s + U] :
    queue.append(s + U)
    visit[s + U] = True
    click[s + U] = click[s] + 1

  if s - D >= 1 and not visit[s - D] :
    queue.append(s - D)
    visit[s - D] = True
    click[s - D] = click[s] + 1

if click[G] == 0 and G != S:
  print('use the stairs')

else:
  print(click[G])

