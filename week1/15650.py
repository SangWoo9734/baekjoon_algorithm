import sys

N, M = map(int, sys.stdin.readline().split(' '))

def nCr (n, arr) :
  if n == N + 1 :
    if len(arr) == M:
      print(' '.join(map(str, arr)))
    return
  
  arr.append(n)
  nCr(n + 1, arr)
  arr.pop()
  nCr(n + 1, arr)

nCr(1, [])