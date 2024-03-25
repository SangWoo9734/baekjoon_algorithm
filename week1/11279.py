import sys
import heapq

N = int(sys.stdin.readline())
numbers = [ int(sys.stdin.readline()) for _ in range(N) ]

hq = []

for n in numbers:
  match n:
    case 0:
      if len(hq) == 0:
        print(0)
      else:
        print(heapq.heappop(hq)[1])
    case _:
      heapq.heappush(hq, [n * -1, n])