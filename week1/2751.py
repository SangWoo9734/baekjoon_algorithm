import sys

N = int(sys.stdin.readline())

numbers = [ int(sys.stdin.readline()) for _ in range(N)]

def merge_sort(arr, left, right):
  if left < right:
    # print(f'left: {left}, right: {right}')
    n = len(arr)
    center = (left + right) // 2

    merge_sort(arr, left, center)
    merge_sort(arr, center + 1, right)

    buffer_inject_index = buffer_search_index = 0
    arr_search_index = arr_inject_index = left

    while arr_search_index <= center:
      # print(buffer_inject_index, arr_search_index, center)
      buffer[buffer_inject_index] = arr[arr_search_index]
      buffer_inject_index += 1
      arr_search_index += 1
    
    while arr_search_index <= right and buffer_search_index < buffer_inject_index:
      if buffer[buffer_search_index] <= arr[arr_search_index]:
        arr[arr_inject_index] = buffer[buffer_search_index]
        buffer_search_index += 1
        
      else:
        arr[arr_inject_index] = arr[arr_search_index]
        arr_search_index += 1

      arr_inject_index += 1

    while buffer_search_index < buffer_inject_index:
      arr[arr_inject_index] = buffer[buffer_search_index]
      buffer_search_index += 1
      arr_inject_index += 1
  


buffer = [ None ] * N
merge_sort(numbers, 0, N - 1)

for i in numbers:
  print(i)