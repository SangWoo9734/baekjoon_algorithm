import sys

input = sys.stdin.readline

N, K = map(int, input().split())

words = [ input().rstrip() for _ in range(N) ]



is_learn = [ 0 for _ in range(26) ]


for w in words:
  for l in w:
    index = ord(l) - ord("a")
    print(index)
    is_learn[index] = 1

print(*is_learn)

count = 0
for w in words:
  res = w
  for l in range(len(is_learn)):
    if is_learn[l]:
      letter = chr(l+ ord("a"))
      print(letter)
      res = res.replace(letter, "", w.count(letter))
  print(res)
  if  res:
    count += 1

print(count)