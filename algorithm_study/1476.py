import sys

input = sys.stdin.readline


E, S, M = map(int, input().rstrip().split(' '))

ey = sy = my = y = 0

while ey != E or sy != S or my != M:
  ey = y % 15 + 1
  sy = y % 28 + 1
  my = y % 19 + 1
  y += 1

  
  # print(f'ey: {ey}, sy: {sy}, my: {my}')
print(y)


# 15x + 1 == 28y + 2 == 19z + 3 == ?

# solution 1
# while (y - E) % 15 != 0 or (y - S) % 28 != 0 or (y - M) % 19 != 0:
#   y += 1

# solution 2 -- ??
e, s, m = map(int, input().split())
all = 15 * 28 * 19
x = (6916 * e + 4845 * s + 4200 * m) % all
if x == 0:
    x = all
print(x)