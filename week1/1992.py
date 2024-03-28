import sys

input = sys.stdin.readline

N = int(input())

quad = [ list(map(int, input()[:-1])) for _ in range(N) ]

def check_black(q):
  for x in q:
    if 1 in x:
      return False
  
  return True

def check_white(q):
  for x in q:
    if 0 in x :
      return False
  
  return True

def check_quad(q):

  # print(q)

  if check_black(q): return 0
  if check_white(q): return 1

  splited_quad = [ [], [], [], [] ]

  for i in range(len(q)):
    half_index =  len(q) // 2
    if i < half_index:
      splited_quad[0].append(q[i][:half_index])
      splited_quad[1].append(q[i][half_index:])

    else:
      splited_quad[2].append(q[i][:half_index])
      splited_quad[3].append(q[i][half_index:])

  # print(splited_quad)
  child_quads =  [ check_quad(q) for q in splited_quad ]

  return '(' + ''.join(map(str, child_quads)) + ')'

print(check_quad(quad))