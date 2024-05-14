import sys
from itertools import combinations

input = sys.stdin.readline

v = 'aeiou'

L, C = map(int, input().split())

letters = input().rstrip().split()


consonants = []
vowel = []
total_combis = []

for l in letters: # 자, 모음 분리
  if l in v:
    vowel.append(l)
  else:
    consonants.append(l)

vowel.sort()
consonants.sort()

for v_c in range(1, (len(vowel) if (L - 2) > len(vowel) else (L - 2)) + 1):
  vowel_combi = list(combinations(vowel, v_c))
  consonant_combi = list(combinations(consonants, L - v_c))

  for v_combi in vowel_combi:
    for c_combi in consonant_combi:
      combi = ''.join(sorted(v_combi + c_combi))
      total_combis.append(combi)

print(*sorted(total_combis), sep='\n')


# 아이디어
# L, C = map(int, input().split())
# letters = input().rstrip().split()

# letters.sort()

# vowels = set('aeiou')

# combis = list(combinations(letters, L))

# for c in combis:
#   diff = set(c) - vowels
  
#   if len(diff) >= 2 and L - len(diff) >= 1:
#     print(''.join(c))
