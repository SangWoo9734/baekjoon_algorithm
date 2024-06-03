import sys

input = sys.stdin.readline

N = int(input())

adj = [list( map(int, input().split()) )for _ in range(N - 1) ]

res_ex = list(map(int, input().split()))

sorted_adj = list(map(list, permutations(adj, N - 1)))

cases = []

res = []

for sa in sorted_adj:
  sa.sort(key= lambda x: x[0])

  if sa not in cases:
    cases.append(sa)

print(*cases, sep='\n')


for case in cases:

  adj_list = [ [] for _ in range(N + 1) ]
  
  for a in case:
    i, j = a

    adj_list[i].append(j)
    adj_list[j].append(i)

  # print(*adj_list, sep='\n')

  case_res = [1]
  visited = [ False ] * ( N + 1 )

  q = deque()
  q.append(1)
  visited[1] = True

  while q:
    cur = q.popleft()

    for i in adj_list[cur]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        case_res.append(i)

  # print(case_res)

  # print("----------")

  if case_res not in res:
    res.append(case_res)

# print(res)
print( 1 if res_ex in res else 0 )


# import sys
# from collections import deque
# from itertools import permutations, combinations

# input = sys.stdin.readline

# N = int(input())

# adj = [list( map(int, input().split()) )for _ in range(N - 1) ]

# res_ex = list(map(int, input().split()))

# sorted_adj = list(map(list, permutations(adj, N - 1)))

# cases = []

# res = []

# for sa in sorted_adj:
#   sa.sort(key= lambda x: x[0])

#   if sa not in cases:
#     cases.append(sa)

# print(*cases, sep='\n')


# for case in cases:

#   adj_list = [ [] for _ in range(N + 1) ]
  
#   for a in case:
#     i, j = a

#     adj_list[i].append(j)
#     adj_list[j].append(i)

#   # print(*adj_list, sep='\n')

#   case_res = [1]
#   visited = [ False ] * ( N + 1 )

#   q = deque()
#   q.append(1)
#   visited[1] = True

#   while q:
#     cur = q.popleft()

#     for i in adj_list[cur]:
#       if not visited[i]:
#         visited[i] = True
#         q.append(i)
#         case_res.append(i)

#   # print(case_res)

#   # print("----------")

#   if case_res not in res:
#     res.append(case_res)

# # print(res)
# print( 1 if res_ex in res else 0 )