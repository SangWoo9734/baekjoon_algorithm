import sys

now = int(sys.stdin.readline())

words = [ sys.stdin.readline()[:-1] for _ in range(now)]

words = list(set(words))
words.sort()
words.sort(key=len)

for word in words:
  print(word)
