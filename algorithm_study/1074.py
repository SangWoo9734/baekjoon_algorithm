import sys

input = sys.stdin.readline

N, r, c = map(int, input().split())

def find_number(n, r, c, count):
  if n == 0:
    # print('fin.')
    return count

  # print(f'1: {n}')
  position_in_square = [ r >= 2 ** (n - 1), c >= 2 ** (n - 1) ]
  # print(f'res: {position_in_square}, r: {r}, c: {c}')
  if position_in_square == [False, True]: # 2사분면
    # print('2분면')
    count += 2 ** (2*(n - 1)) * 1
    c -= 2 ** (n - 1)
  elif position_in_square == [True, False]: # 3사분면
    # print('3분면')
    count += 2 ** (2*(n - 1)) * 2
    r -= 2 ** (n - 1)

  elif position_in_square == [True, True]: # 4사분면
    # print('4분면')
    count += 2 ** (2*(n - 1)) * 3
    c -= 2 ** (n - 1)
    r -= 2 ** (n - 1)
  
  # print(f'2: {n}')

  return find_number( n - 1, r, c, count )

print(find_number(N, r, c, 0))
