import sys

number_count = int(sys.stdin.readline())

numbers = [ int(sys.stdin.readline()) for _ in range(number_count)]

sorted_number = sorted(numbers)

for i in sorted_number:
  print(i)

# 2751 문제도 이걸로 품