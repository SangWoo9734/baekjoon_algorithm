import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  N = int(input())

  employees = []

  for i in range(N):
    employees.append(list(map(int, input().split())))

  employees = sorted(employees)

  print(employees)
  
  total = 0
  min_value = N + 1
  for e in employees:
    _, val = e

    if min_value > val:
      total += 1
      min_value = val

    if min_value == 1:
      break


  print(total)