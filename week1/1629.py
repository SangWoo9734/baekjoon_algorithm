import sys

input = sys.stdin.readline


A, B, C = list(map(int, input()[:-1].split(' ')))

res = []
value = A
times = 0

def multiply(a, b, c):
  if b == 1:
    return a % c


  if b % 2:
    return (multiply(a,  b // 2, c ) ** 2) * a % c
  
  return (multiply(a, b // 2, c ) ** 2) % c


print(multiply(A, B, C))
