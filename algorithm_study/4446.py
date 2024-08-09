import sys

consonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']
vowel = ['a', 'i', 'y', 'e', 'o', 'u']

lines = sys.stdin.readlines()

for line in lines:
  target = list(line.rstrip())
  res = ''
  for index in range(len(target)):
    is_upper = False


    l = target[index]

    if l.isupper():
      is_upper = True
    
    l = l.lower()

    if l in vowel:
      index = vowel.index(l)
      index = (index + 3) % len(vowel)

      res += vowel[index].upper() if is_upper else vowel[index]
    
    elif l in consonant:
      index = consonant.index(l)
      index = (index + 10) % len(consonant)

      res += consonant[index].upper() if is_upper else consonant[index]
    else:
      res += target[index]

  print(res)