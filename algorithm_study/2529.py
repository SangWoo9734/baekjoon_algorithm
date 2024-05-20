import sys
from itertools import permutations

def check(value, inequality):
  for i in range(len(inequality)):
    if inequality[i] == '>':
      if  value[i] < value[i + 1]:
        return False
    else:
      if  value[i] > value[i + 1]:
          return False

  return True

input = sys.stdin.readline

k = int(input())

inequality = input().rstrip().split()

combi = list(permutations(list(map(str, list(range(0, 10)))), k + 1))

max_combi = '0' * (k + 1)
min_combi = '9' * (k + 1)

# print(check(['9','8','7'], inequality))

for c in combi:
  
  if not check(c, inequality): continue

  # print(check(['9', '8', '7']))

  target = ''.join(c)

  # print(f'max_combi: {max_combi}, target: {target}')

  if max_combi < target:
    max_combi = target
  
  if min_combi > target:
    min_combi = target


print(max_combi)
print(min_combi)