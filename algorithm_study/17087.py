import sys
# from math import gcd

input = sys.stdin.readline

def GCD(a, b):
  if a == 0: return b

  return GCD(b%a, a)

N, S = map(int, input().split())

brothers = list(map(int, input().split()))

dist_abs = [ abs(b - S) for b in brothers ]

dist_gcd = dist_abs[0]

for dist in dist_abs[1:]:
  a, b = (dist_gcd, dist) if dist < dist_gcd else (dist, dist_gcd)

  dist_gcd = GCD(a, b)
  # dist_gcd = gcd(dist, dist_gcd)


print(dist_gcd)