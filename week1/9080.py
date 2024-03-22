import math, sys

def get_prime_numbers(n):
  is_prime = [ True for _ in range(n + 1)]

  is_prime[0] = False
  is_prime[1] = False

  for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]:
      j = 2

      while i * j <= n:
        is_prime[i * j] = False
        j += 1

  prime_number = []

  for check_prime, number in zip(is_prime, range(n + 1)):
    if check_prime:
      prime_number.append(number)
  
  return prime_number



count = int(sys.stdin.readline())
numbers = [ int(sys.stdin.readline()) for _ in range(count)]
max_numbers = max(numbers)
prime_number = get_prime_numbers(max_numbers)

for n in numbers:

  value1 = 0
  value2 = 0

  p = [ value for value in filter(lambda x: x <= (n //2), prime_number)][::-1]

  for v in p:

    if (n - v) in prime_number:
      value1, value2 = sorted([v, n-v])
  

      print(value1, value2)
      break