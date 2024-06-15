import sys

input = sys.stdin.readline

N = int(input())

small = N

start_index = 0 if N - 9 * len(str(N)) < 0 else N - 9 * len(str(N))

for x in range(start_index, N + 1):
  sumOfElement = sum(map(int, list(str(x))))
  if (x + sumOfElement == N):
    small = x
    break

if small == N:
  print(0)
else:
  print(x)