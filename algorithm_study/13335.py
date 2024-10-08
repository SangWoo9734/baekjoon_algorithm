import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())

trucks = list(map(int, input().split()))

next_truck_index = 0
cur_truck = deque([])
cur_truck_time = deque([])

t = 0

while True:
  t += 1
  for i in range(len(cur_truck_time)):
    cur_truck_time[i] += 1

  if len(cur_truck) > 0:
    if cur_truck_time[0] > w:
      deque.popleft(cur_truck)
      deque.popleft(cur_truck_time)

  if len(trucks) > next_truck_index and sum(cur_truck) + trucks[next_truck_index] <= L:
    deque.append(cur_truck, trucks[next_truck_index])
    deque.append(cur_truck_time, 1)
    next_truck_index += 1

  if len(cur_truck) == 0:
    break



print(t)
