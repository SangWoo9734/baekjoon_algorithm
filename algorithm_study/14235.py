import sys
import heapq

input = sys.stdin.readline

N = int(input())

bag = []

for _ in range(N):
  command = list(map(int, input().split()))
  if command[0] == 0:
    if len(bag) == 0:
      print(-1)
    else:
      print(-1 * heapq.heappop(bag))
  else:
    for index in range(1, command[0] + 1):
      heapq.heappush(bag, command[index] * -1);
    