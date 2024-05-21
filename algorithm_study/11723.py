import sys

input = sys.stdin.readline

M = int(input())

# s = [ 0 ] * 21 

# for _ in range(M):
#   c = input().split()
  
#   # print(c)
#   if c[0] == 'add':
#     s[ int(c[1]) ] = 1

#   elif c[0] == 'check':
#     print(s[ int(c[1]) ])

#   elif c[0] == 'remove':
#     s[ int(c[1]) ] = 0

#   elif c[0] == 'toggle':
#     s[ int(c[1]) ] = not s[ int(c[1]) ]

#   elif c[0] == 'all':
#     s = [1] * 21

#   elif c[0] == 'empty':
#     s = [0] * 21

s = [ False ] * 21 

for _ in range(M):
  c = input().split()
  
  # print(c)
  if c[0] == 'add':
    s[ int(c[1]) ] = True

  elif c[0] == 'check':
    print(int(s[ int(c[1]) ]))

  elif c[0] == 'remove':
    s[ int(c[1]) ] = False

  elif c[0] == 'toggle':
    s[ int(c[1]) ] = not s[ int(c[1]) ]

  elif c[0] == 'all':
    s = [ True ] * 21

  elif c[0] == 'empty':
    s = [ False ] * 21


# 비트마스킹을 활용한 풀이
import sys
input = sys.stdin.readline

bit = 0b0

M = int(input())

for i in range(M):
    order = input().split()

    if order[0] == 'add':
        bit |= (0b1 << int(order[1]))
    elif order[0] == 'remove':
        bit &= ~(0b1 << int(order[1]))
    elif order[0] == 'check':
        print(0b1 if bit & (0b1 << int(order[1])) != 0 else 0)
    elif order[0] == 'toggle':
        bit ^= (0b1 << int(order[1]))
    elif order[0] == 'empty':
        bit = 0b0
    elif order[0] == 'all':
        bit = 0b111111111111111111111