import sys

test_time = int(sys.stdin.readline())

for _ in range(test_time):
  multi_times, words = sys.stdin.readline()[:-1].split(' ')

  for letter in words:
    print(letter * int(multi_times), end='')

  print()