import heapq
import sys

input = sys.stdin.readline

N = int(input())

ramens = [ tuple(map(int, input().split())) for _ in range(N) ]

ramens.sort()

dead_day = max([ r[0] for r in ramens ])

time = 1
index = 0

cur_ramens = []

while time <= dead_day :
  while index < N:
    if ramens[index][0] == time:
      heapq.heappush(cur_ramens, (ramens[index][1], ramens[index][0]))
      index += 1
    else:
      break

  while len(cur_ramens) > time:
    heapq.heappop(cur_ramens)


  
  time += 1


print(sum([ r[0] for r in cur_ramens]))
