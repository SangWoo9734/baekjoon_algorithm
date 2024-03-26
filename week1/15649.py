import sys

N, M = map(int, sys.stdin.readline().split(' '))

check = [ False ] * N
result = [ 0 ] * M

def nPr (n) : 
  # print(f'n : {n}')
  if n == M:
    print(' '.join(map(str, result)))
    return

  for index in range(N):
    # print(f'running!{index}')
    if check[index] == False:
      check[index] = True
      result[n] = index + 1
      # print(f'before index {index}')
      # print(result)
      nPr(n + 1)
      # print(f'after index {index}')
      check[index] = False

  # print('--------------')

nPr(0)