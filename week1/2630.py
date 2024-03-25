import sys

def is_blue (paper):
  for row in paper:
    if 0 in row:
      return False

  return True

def is_white (paper):
  for row in paper:
    if 1 in row:
      return False

  return True

def cut_paper(paper):
  if is_blue(paper):
    return { 'blue': 1, 'white': 0 }

  if is_white(paper):
    return { 'blue': 0, 'white': 1 }

  splited_papers = [ [], [], [], [] ]

  for i in range(len(paper)):
    half_index =  len(paper) // 2
    if i < half_index:
      splited_papers[0].append(paper[i][:half_index])
      splited_papers[1].append(paper[i][half_index:])

    else:
      splited_papers[2].append(paper[i][:half_index])
      splited_papers[3].append(paper[i][half_index:])
  
  result = [ cut_paper(cutted_paper) for cutted_paper in splited_papers ]
  total = { 'blue': 0, 'white': 0 }

  for r in result:
    total['blue'] += r['blue']
    total['white'] += r['white']

  return total

N = int(sys.stdin.readline())

paper = [ list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
result = cut_paper(paper)

print(result['white'])
print(result['blue'])