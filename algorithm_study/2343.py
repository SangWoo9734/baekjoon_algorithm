import sys

input = sys.stdin.readline

def count_video (arr, mid):

  size = 0
  count = 0
  for a in arr:
    size += a
    if size >= mid:
      count += 1
      size = a

  return count




N, M = map(int, input().split())

time = list(map(int, input().split()))

pl = 1
pr = sum(time)

def binary_search(pl, pr, res):
  # print(f'pl: {pl}, pr:{pr}, res: {res}')
  if pl > pr:
    return res

  mid = ( pl + pr ) // 2

  vc = count_video(time, mid)

  if vc > M:
    return binary_search(mid + 1, pr, res)
  else:
    if vc == M:
      res.append(mid)
    return binary_search(pl, mid - 1, res)

print(max(binary_search(pl, pr, [])))