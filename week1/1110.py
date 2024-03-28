import sys

input = sys.stdin.readline

N = int(input())
his = []

def check(n):
  his.append(n)

  x = n // 10 + n % 10
  y = (n % 10) *  10 + x % 10

  print(y)

  if y == N:
    # print(his)
    return
  
  else:
    check(y)

check(N)

print(len(his))

# 반복
# ran = num
# count = 0
# a = 0
# b = 0

# while True:
#     a = num//10 + num%10
#     b = (num%10)*10 + a%10
#     count += 1
#     num = b
#     if b == ran:
#         break

# print(count)
