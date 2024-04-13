import sys
from math import gcd
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N = int(input())

cases = [ list(map(int, input().split()))[1:] for _ in range(N) ]


# for c in cases:
#   combi_cases = list(combinations(c, 2))
#   # print(combi_cases)
#   total = 0
#   for cc in combi_cases:
#     a, b = cc
#     # print(f'cc: {cc}, gcd: {gcd(a, b)}')
#     total += gcd(a, b)

  
#   print(total)


def gcd(n, m):
  for i in range(max(n, m), 0, -1):
    if n % i == 0 and m % i == 0:
      return i


for c in cases:
  total = 0
  for i in range(len(c)):
    for j in c[i + 1:]:
      total += gcd(c[i], j)

  print(total)