import sys

input = sys.stdin.readline

N = int(input())

res = [ 1, 1 ] + [ 0 ] * ( N - 1 )

def fibo(n):
  if not res[n]:
    res[n] = res[n - 1] + res[n - 2]

for i in range(2, N + 1):
    fibo(i)

print( res[N] % 15746 )