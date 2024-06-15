import sys

input = sys.stdin.readline

N = int(input())

for x in range(1, N + 1):
  sumOfElement = sum(map(int, list(str(x))))
  if (x + sumOfElement == N):
    break

if x == N:
  print(0)
else:
  print(x)