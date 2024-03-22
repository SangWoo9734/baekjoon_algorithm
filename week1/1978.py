import sys
import math

count = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split(' ')))


max_num = max(numbers)

is_prime = [ True for i in range(max_num + 1)]

for n in range(2, int(math.sqrt(max_num)) + 1):
  if is_prime[n]:
    j = 2

    while j * n <= max_num:
      is_prime[j * n] = False
      j += 1

count = 0
for n in numbers:
  if is_prime[n] and n != 1 and n != 0:
    count += 1

print(count)