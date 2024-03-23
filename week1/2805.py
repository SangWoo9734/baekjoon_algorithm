import sys

number_of_tree, tree_length = list(map(int, sys.stdin.readline().split(' ')))

trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

while low + 1 < high:
  cut_position = (high + low) // 2

  # 상근이가 얻은 나무
  earning_length = 0 
  for tree in trees:
    if tree > cut_position :
      earning_length += tree - cut_position

  # 결정 함수
  # 매개변수 위치 조정
  if  earning_length >= tree_length:
    low = cut_position

  else:
    high = cut_position


print(low)
  