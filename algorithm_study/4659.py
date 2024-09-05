import sys

input = sys.stdin.readline

while True:

  word = input().rstrip()

  if word == 'end': break

  else:
    vowel = set('aeiou')

    is_acceptable = True

    if len(list(set(word) & vowel)) == 0:
      is_acceptable = False

    vowel_count = 0
    consonant_count = 0

    for index in range(len(word)):
      if word[index] in vowel:
        vowel_count += 1
        consonant_count = 0
      else:
        consonant_count += 1
        vowel_count = 0
      
      if vowel_count == 3 or consonant_count == 3:
        is_acceptable = False
      
      if index > 0 and word[index] == word[index - 1] and word[index] != 'o' and word[index] != 'e':
        is_acceptable = False

    if is_acceptable:
      print(f'<{word}> is acceptable.')
    else:
      print(f'<{word}> is not acceptable.')