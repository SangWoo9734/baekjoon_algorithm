import sys
from itertools import combinations
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n, m = map(int, input().split())

no2 = 0
no5 = 0




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

print(no2 if no2 < no5 else no5)