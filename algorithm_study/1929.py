import sys


input = sys.stdin.readline

A, B = map(int, input().split())

is_prime = [ True, False, False ] + [ False ] * ( B - 2 )

for i in range(2, B + 1):
  if is_prime[i] == False:
    j = 1
    while True:
      j += 1
      if i * j > B : break
      is_prime[i * j] = True

    if i >= A:
      print(i)

# print(is_prime)
