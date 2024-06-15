import sys

input = sys.stdin.readline

ss = input().rstrip()

target = list(input().rstrip())

stack = []

for char in ss:
  stack.append(char)

  if target == stack[-1 * len(target):]:
    for _ in range(len(target)):
      stack.pop()

if not stack:
  print("FRULA")
else:
  print(*stack, sep='')


# before_ss = ss
# ss = ss.replace(target, '')

# while(before_ss != ss):
#   before_ss = ss
#   ss = ss.replace(target, '')

# if not ss:
#   print("FRULA")
# else:
#   print(*before_ss, sep='')