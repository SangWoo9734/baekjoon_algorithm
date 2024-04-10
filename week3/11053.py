import sys

input = sys.stdin.readline

A = int(input())

nums = list(map(int, input().split()))

num_with_LIS = [0] * A

LIS = [0]

for i in range( A ):

  for n, j in zip(LIS, range(len(LIS))):
    if n >= nums[i]:
      LIS[j] = nums[i]
      num_with_LIS[i] = j
      break
      
    if j == (len(LIS) - 1):
      LIS.append(nums[i])
      num_with_LIS[i] = len(LIS)

  # print(LIS)
    
print(len(LIS) - 1)

