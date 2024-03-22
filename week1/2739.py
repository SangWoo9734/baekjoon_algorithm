import sys

target = int(sys.stdin.readline())

for i in range(1, 10):
  print(f'{ target } * { i } = { target * i }')