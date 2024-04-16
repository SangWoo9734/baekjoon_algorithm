import sys
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, m = map(int, input().split())


# for i in range(m, n + 1):
#   while(i !=0 and (i % 2 == 0 or i % 5 == 0)):
#     if (i % 2 == 0):
#       no2 += 1
#       i = i // 2

#     if (i % 5 == 0):
#       no5 += 1
#       i = i // 5

# for i in range(1, m):
#   while(i !=0 and (i % 2 == 0 or i % 5 == 0)):
#     if (i % 2 == 0):
#       no2 -= 1
#       i = i // 2

#     if (i % 5 == 0):
#       no5 -= 1
#       i = i // 5

def count_n(N, S):
  count = 0
  while N >= S:
    count += N // S
    N //= S

  return count

cnt_2 = count_n(n, 2) - count_n(n - m, 2) - count_n(m, 2)
cnt_5 = count_n(n, 5) - count_n(n - m, 5) - count_n(m, 5)

print(cnt_2 if cnt_2 < cnt_5 else cnt_5)