import sys

num_list = [ int(sys.stdin.readline()) for _ in range(9) ]

max_num = max(num_list)
max_num_index = num_list.index(max_num) + 1

print(max_num)
print(max_num_index)
