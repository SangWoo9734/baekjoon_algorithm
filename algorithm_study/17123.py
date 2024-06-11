import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
  N, M = map(int, input().split())
  
  board = [ list(map(int, input().split())) for _ in range (N) ]

  actions = [ list(map(int, input().split())) for _ in range (M) ]

  total_row = [ 0 ] * N
  total_col = [ 0 ] * N

  for i in range(N):
    for j in range(N):
      total_row[j] += board[i][j]
      total_col[i] += board[i][j]


  for a in actions:
    r1, c1,  r2, c2, v = a
    
    for i in range(r1 - 1, r2):
      total_col[i] += v * ( c2 - c1 + 1 )
    for j in range(c1 - 1, c2):
        # print(f"i: {i}, j: {j}")
      total_row[j] += v * ( r2 - r1 + 1 )


    # print()



  print(*total_col)
  print(*total_row) 
