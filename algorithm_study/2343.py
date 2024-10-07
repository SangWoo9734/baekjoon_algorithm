import sys

input = sys.stdin.readline

def count_video (arr, mid):

  size = 0
  count = 1
  for a in arr:
    size += a

    if size > mid:
      count += 1
      size = a

  return count




N, M = map(int, input().split())

time = list(map(int, input().split()))

pl = max(time)
pr = sum(time)
res = 10000000000

while pl <= pr:

  mid = ( pl + pr ) // 2

  vc = count_video(time, mid)
  # print(f'pl: {pl}, pr:{pr}, mid:{mid} vc: {vc}')

  if vc > M: 
    pl = mid + 1
  else:
    pr = mid - 1

print(pl)