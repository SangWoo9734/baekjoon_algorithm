import sys

number_of_target = int(sys.stdin.readline())
target_numbers = list(map(int, sys.stdin.readline().split(' ')))

number_of_case = int(sys.stdin.readline())
case_numbers = list(map(int, sys.stdin.readline().split(' ')))

def binary_search(case, target_numbers):
  pl = 0
  pr = len(target_numbers) - 1

  while True:
    pc = (pr + pl) // 2

    if target_numbers[pc] == case:
      return 1

    elif target_numbers[pc] < case:
      pl = pc + 1
    
    else:
      pr = pc - 1
  
    if pl > pr:
      break

  return 0

sorted_target_numbers = sorted(target_numbers)
for case in case_numbers:
  print(binary_search(case, sorted_target_numbers))