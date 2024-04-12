import sys


input = sys.stdin.readline

A, B = map(int, input().split())

A, B = (A, B) if A > B else (B, A)

# gcc
for i in range(B, 0, -1):
  if A % i == 0 and B % i == 0:
    print(i)
    break

#lcm
a = A
b = B

while a != b:
  if a > b:
    b += B
  elif b > a:
    a += A

print(a)
