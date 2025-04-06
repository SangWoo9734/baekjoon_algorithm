import sys
from itertools import combinations

input = sys.stdin.readline

N, C = map(int, input().split())
items = list(map(int, input().split()))

mid = N // 2

arr1 = []

for i in range(0, mid + 1):
  combi = combinations(items[:mid], i)

  for c in combi:
    sum_c = sum(c)
    if sum_c <= C:
      arr1.append(sum_c)

arr2 = []
for i in range(0, N - mid + 1):
  combi = combinations(items[mid:], i)

  for c in combi:
    sum_c = sum(c)
    if sum_c <= C:
      arr2.append(sum_c)

arr2.sort()

total = 0

for a1 in arr1:
  left = 0
  right = len(arr2) - 1

  while left <= right:
    mid = (right - left) // 2 + left

    if arr2[mid] <= C - a1:
      left = mid + 1
    else: 
      right = mid - 1

  total += left

print(total)