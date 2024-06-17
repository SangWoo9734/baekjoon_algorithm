import sys
from itertools import combinations

KS_case = []

while True:
  input_value = input()

  if input_value == "0":
    break

  KS_case.append(list(map(int, input_value.split())))


for c in KS_case:
  k = c [0]
  s = c [1:]

  for combi in list(combinations(s, 6)):
    print(*combi, sep=" ")


  print()