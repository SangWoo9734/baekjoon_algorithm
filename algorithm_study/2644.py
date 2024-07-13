import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())

A, B = map(int, input().split())

K = int(input())

family = [ [] for _ in range(N + 1) ]
visit = [ False for _ in range(N + 1) ]

for _ in range(K):
  x, y = map(int, input().split())

  family[x].append(y)
  family[y].append(x)

visit[A] = True
q = deque([[A, 0]])

count = -1

while q:
  number, res = q.pop()

  if number == B:
    count = res
    break

  for n in family[number]:
    if visit[n] == False:
      visit[n] = True
      q.append([n, res + 1])

print(count)

