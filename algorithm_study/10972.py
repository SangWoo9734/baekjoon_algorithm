import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

nums = list(map( int, input().split() ))

p = list(map(list, permutations(sorted(nums), len(nums))))


# print(*p, sep='\n')

# if p[-1] == nums:
#   print(-1)
# else:
#   for i in range(len(p) - 1):
#     if p[i] == nums:
#       print(' '.join(map(str, p[i + 1])))


if nums == sorted(nums)[::-1]:
  print(-1)

else:
  nums.reverse() # [ 3 2 1 5 4 ] -> 역순으로 봤을때
  # print(nums)

  for i in range(N): 
    if nums[i] > nums[i + 1]: # [ 3 2 (1 5) 4 ] -> 5 -> 1에서 내림차순이 끊김
      partial = nums[:i + 2] # [ 3 2 / 1 5 4 ] -> 1을 포함한 3개의 숫자로 재정렬
      # print(f'partial: {partial}')

      partial_sorted = sorted(partial) # 하위 배열 정렬 [ 1, 4, 5 ]
      # print(f'partial_sorted: {partial_sorted}')

      next_index = partial_sorted.index(nums[i + 1]) + 1# 4에 대한 인덱스 계산 -> 1
      # print(f'next_index: {next_index}')

      new_partial = []
      for j in range(len(partial_sorted)):
        if j != next_index:
          new_partial.append(partial_sorted[j])
      
      new_partial.reverse()
      new_partial.append(partial_sorted[next_index]) 

      new_list_reversed = new_partial + nums[i + 2:]

      print(' '.join(map(str, reversed(new_list_reversed))))      
      break

# [ 3 2 1 5 4 ] -> 역순으로 봤을때
# [ 3 2 (1 5) 4 ] -> 5 -> 1에서 내림차순이 끊김
# [ 3 2 / 1 5 4 ] -> 1을 포함한 3개의 숫자를 재정렬
# [ 3 2 / 4 5 1 ] -> 타겟 숫자들 중 1 다음으로 큰 수와 스왑
# [ 3 2 4 1 5 ] -> 정렬된 수 (4) 이하 수들은 오름차순으로 정렬