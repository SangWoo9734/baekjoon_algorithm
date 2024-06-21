import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

N, K = map(int, input().split());

lan = [ int(input()) for _ in range(N) ]

pl = 1
pr = max(lan)

def binary_search(pl, pr):
  if pl > pr:
    return pr
  
  # print(f'pr: {pr} / pl: {pl}')
  mid = (pr + pl) // 2

  total = 0
  for l in lan:
    total += l // mid

  if K <= total:
    return binary_search(mid + 1, pr)
  else:
    return binary_search(pl, mid - 1)




print(binary_search(1, max(lan)))