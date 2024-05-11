import sys

input = sys.stdin.readline

# n = input().rstrip()

# l = len(n)
# N = int(n)

# i = l
# count = 0

# while i > 0:
#   if i == 1:
#     count += N if N < 9 else 9
#   elif i == l:
#     count += i * (N -  (10 ** (i - 1)) + 1)
#   else:
#     count += i * (10 ** i - 10 ** (i - 1))

#   i -= 1


N = int(input())

count = 0

j = 1
while (1) :
  if N < 10 ** j:
    count += j * (N - 10 ** (j - 1) + 1)
    break
  else:
    count += j * (10 ** j - 10 ** (j - 1))

  j += 1

print(count)


