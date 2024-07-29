import sys

input = sys.stdin.readline

p, m = map(int, input().split())

rooms = []

for _ in range(p):
  no_room = True
  level, name = input().split()
  level = int(level)

  if len(rooms) == 0:
    rooms.append([[name, level]])
    continue

  for r in rooms:
    standard_lv = r[0][1]
    # print(f'name: {name}, is10: {standard_lv - 10 <= level <= standard_lv + 10}, len5: {len(r)< m}')
    if name in [i[0] for i in r]:
      no_room = False 
      break
    
    if standard_lv - 10 <= level <= standard_lv + 10 and len(r) < m:
      r.append([name, level])
      no_room = False 
      break

  if no_room:
    rooms.append([[name, level]])

for r in rooms:
  if len(r) == m:
    print('Started!')
  else:
    print('Waiting!')

  joined_mem = [ str(mem[1]) + " " + mem[0]  for mem in sorted(r, key=lambda x : x[0])]
    

  print(*joined_mem, sep='\n')
