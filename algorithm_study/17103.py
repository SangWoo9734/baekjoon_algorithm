import sys

input = sys.stdin.readline

T = int(input())

nums = [ int(input()) for _ in range(T) ]

# 에라토스
max_nums = max(nums)

check = [ False ] * ( max_nums + 1 )

for c in range(2, max_nums + 1):
  if check[c] == True: continue

  j = 2

  while c * j <= max_nums:
    check[c * j] = True

    j += 1

# 골바
for n in nums:
  if n == 2:
    print(0)
  else:
    half = n // 2
    count = 0
    for c in range(2, half + 1):
      if check[n - c] == False and check[c] == False:
        count += 1

    print(count)

