import sys

input = sys.stdin.readline

N, M = map(int, input().split())

cake = list(map(int, input().split()))

cake = sorted(cake)
cake = sorted(cake, key = lambda x : x % 10)
res = 0

for c in cake:
  if c == 10:
    res += 1
  else:
    while c > 10 and M > 0:
      c -= 10
      M -= 1
      res += 1

    if c == 10:
      res += 1
  

print(res)
