import sys
import heapq

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split(' ')))

result1 = [0] * N
result2 = [0] * N
hq = []

for i in range(N - 1, -1, -1):
  while hq and hq[0][0] < towers[i]:
    t, idx = heapq.heappop(hq)
    result1[idx] = i + 1
  
  heapq.heappush(hq, (towers[i], i))

  print(hq)


print(" ".join(map(str, result1)))

print('--------------v-----------------------------------')
ts = []

for i in range(N - 1, -1 ,-1):
  while ts and ts[0][0] < towers[i]:
    t, index = ts.pop()
    result2[index] = i + 1
  
  ts.append([towers[i], i])

  
  print(ts)

print(" ".join(map(str, result2)))

  
